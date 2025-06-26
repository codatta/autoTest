import requests
import threading
import time
import random
import json
from web3.auto import w3
from eth_account.messages import encode_defunct

# 配置参数
BASE_URL = "https://app-test.b18a.io"  # 基础API地址
CONCURRENCY = 50  # 并发数
TOTAL_REQUESTS = 500  # 总请求数
WALLET_COUNT = 100  # 预生成钱包数量
CHAIN_ID = "56"  # 链ID，根据curl命令中的参数设置

# 公共请求头（从curl命令中提取）
COMMON_HEADERS = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "content-type": "application/json",
    "origin": "https://app-test.b18a.io",
    "priority": "u=1, i",
    "referer": "https://app-test.b18a.io/account/signin?from=%2Fapp",
    "sec-ch-ua": '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}


# 生成测试钱包
def generate_wallets(count):
    wallets = []
    for _ in range(count):
        account = w3.eth.account.create()
        wallets.append({
            "address": account.address,
            "private_key": account.key.hex()
        })
    return wallets


# 生成签名消息（根据curl命令中的格式）
def generate_sign_message(address, nonce, issued_at):
    message = (
        f"app-test.b18a.io wants you to sign in with your Ethereum account:\n"
        f"{address}\n\n\n"
        f"URI: https://app-test.b18a.io/account/signin?from=%2Fapp\n"
        f"Version: 1\n"
        f"Chain ID: {CHAIN_ID}\n"
        f"Nonce: {nonce}\n"
        f"Issued At: {issued_at}"
    )
    return message


# 模拟单个用户的登录流程
def user_flow(wallet, thread_id, request_id):
    try:
        address = wallet["address"]
        private_key = wallet["private_key"]

        # 1. 请求获取Nonce
        nonce_url = f"{BASE_URL}/api/v2/user/nonce"
        nonce_payload = {"account_type": "block_chain"}

        nonce_resp = requests.post(
            nonce_url,
            headers=COMMON_HEADERS,
            json=nonce_payload,
            timeout=10
        )

        if nonce_resp.status_code != 200:
            return f"Thread {thread_id}, Request {request_id}: 获取Nonce失败，状态码 {nonce_resp.status_code}"

        nonce_data = nonce_resp.json()
        nonce = nonce_data.get("data", {}).get("nonce", "0000000000000000")
        issued_at = nonce_data.get("data", {}).get("issued_at", "2025-06-26T07:33:42.592Z")

        # 2. 生成签名消息并签名
        sign_message = generate_sign_message(address, nonce, issued_at)
        message = encode_defunct(text=sign_message)
        signed_message = w3.eth.account.sign_message(message, private_key=private_key)
        signature = signed_message.signature.hex()

        # 3. 发送登录请求
        login_url = f"{BASE_URL}/api/v2/user/login"
        login_payload = {
            "account_type": "block_chain",
            "account_enum": "C",
            "connector": "codatta_wallet",
            "inviter_code": "",
            "wallet_name": "OKX Wallet",
            "address": address,
            "chain": CHAIN_ID,
            "nonce": nonce,
            "signature": signature,
            "message": sign_message,
            "source": {
                "device": "WEB",
                "channel": "codatta-platform-website",
                "app": "codatta-platform-website"
            }
        }

        login_resp = requests.post(
            login_url,
            headers=COMMON_HEADERS,
            json=login_payload,
            timeout=15
        )

        if login_resp.status_code == 200:
            token = login_resp.json().get("data", {}).get("token")
            return f"Thread {thread_id}, Request {request_id}: 登录成功，Token长度: {len(token) if token else 0}"
        else:
            error_msg = login_resp.json().get("message", "未知错误")
            return f"Thread {thread_id}, Request {request_id}: 登录失败，状态码 {login_resp.status_code}，错误: {error_msg}"

    except Exception as e:
        return f"Thread {thread_id}, Request {request_id}: 异常 - {str(e)[:50]}"


# 压力测试主函数
def stress_test():
    wallets = generate_wallets(WALLET_COUNT)
    print(f"生成 {len(wallets)} 个测试钱包")

    threads = []
    results = []
    success_count = 0
    fail_count = 0

    for i in range(TOTAL_REQUESTS):
        wallet = wallets[i % len(wallets)]  # 循环使用钱包
        thread = threading.Thread(
            target=lambda w, tid, rid: results.append(user_flow(w, tid, rid)),
            args=(wallet, i // CONCURRENCY, i)
        )
        threads.append(thread)
        thread.start()

        # 控制并发数
        if len(threads) >= CONCURRENCY:
            for t in threads:
                t.join()
            threads = []

        # 添加随机延迟，模拟真实用户行为
        time.sleep(random.uniform(0.1, 0.6))

    # 等待剩余线程完成
    for t in threads:
        t.join()

    # 统计结果
    success_count = sum(1 for r in results if "成功" in r)
    fail_count = len(results) - success_count

    print("\n===== 压测结果 =====")
    print(f"总请求数: {len(results)}")
    print(f"成功数: {success_count} ({success_count / len(results) * 100:.2f}%)")
    print(f"失败数: {fail_count} ({fail_count / len(results) * 100:.2f}%)")

    # 输出前10条失败结果
    if fail_count > 0:
        print("\n失败案例示例:")
        failed_results = [r for r in results if "失败" in r or "异常" in r]
        for r in failed_results[:10]:
            print(r)


if __name__ == "__main__":
    stress_test()
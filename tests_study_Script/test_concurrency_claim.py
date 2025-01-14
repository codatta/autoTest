import asyncio
import aiohttp
import logging
from utils.logger import log_execution


# 定义要发送的请求
async def send_request(session, task_id):
    url = "https://app.codatta.io/api/task/verify"
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9",
        "auth_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0aWNrZXRfaWQiOiJjYmUxMzUzZjE4ZTI2YWZjIiwidG9rZW4iOiJleUpoYkdjaU9pSklVekkxTmlJc0luUjVjQ0k2SWtwWFZDSjkuZXlKMWMyVnlYMmxrSWpvaU16ZzNORFF5TlRneU5qVXdPRGd3SWl3aWJHOW5hVzVmZEdsdFpTSTZNVGN6Tmpnek5UUXhNeTQyT1Rjd01YMC5GTG4wejhnSmNxZV8yc1VnS19lZ1RQdVVsQTMwaUFRYXZUQ01FZ1VWMlowIn0.Ty9D0szmIx_w4Qggw-qixRQuM4r_mldRb8WfSW3T1DE",
        "content-type": "application/json",
        "cookie": "_c_WBKFRo=IMngFnzJJyut4wQ4qApIHxq4lgtX8kKp5hcQesqz; _nb_ioWEgULi=",
        "origin": "chrome-extension://doklnekkemmhclakfekoccilofpdcncb",
        "priority": "u=1, i",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "none",
        "showinvitercode": "false",
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMzg3NDQyNTgyNjUwODgwIiwiY29ubmVjdG9yIjoiY29kYXR0YV93YWxsZXQiLCJhY2NvdW50X3R5cGUiOiJibG9ja19jaGFpbiIsImFjY291bnQiOiIweGNkMDE5MWI0YmY4MjE1MjUzMUJjZmY4MUFiNDFBNUI5RERkMENBMzQiLCJsb2dpbl9zb3VyY2UiOiJjb2RhdHRhLXBsYXRmb3JtLXdlYnNpdGUiLCJsb2dpbl93YWxsZXRfc291cmNlIjoiT0tYIFdhbGxldCJ9.uIN78E0r-_CDfaNNZZkCBAt6J1csC7UR2pN8Tp0b3HA",
        "uid": "387442582650880",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "x-client": "Codatta Clip@1.1.6"
    }

    data = {
        "task_id": task_id
    }

    try:
        async with session.post(url, headers=headers, json=data) as response:
            if response.status == 200:
                return await response.json()
            else:
                logging.error(f"Request failed with status: {response.status}")
    except Exception as e:
        logging.error(f"Error sending request: {e}")

# 定义并发任务的函数
async def main():
    task_id = "SUBMIT-INS-DATA"  # 固定的 task_id
    async with aiohttp.ClientSession() as session:
        tasks = [send_request(session, task_id) for _ in range(100)]
        results = await asyncio.gather(*tasks)

        for idx, result in enumerate(results):
            if result:
                print(f"Response {idx + 1}: {result}")
            else:
                print(f"Response {idx + 1}: No valid response")

# 运行并发任务
def test_concurrency_claim():
    asyncio.run(main())


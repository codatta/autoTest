import logging

import requests

from config.configBase import Config
from utils.logger import log_execution


@log_execution
def test_categories():
    logging.info("这是测试访问quest种类的接口")
    url=Config.BASE_URL+"/api/task/categories"

    # 请求头信息
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9",
        "content-length": "0",
        "cookie": "_ga=GA1.1.1344376451.1732246450; Codatta-Medical-WSI-Token=eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6ImNlNTlkYjYxLWEyY2EtNGJjNy05MTI0LWU1MTkxY2U2MGQ3MSJ9.4luKeMey_NK3UVXEclqxJ9THQIyw_pkoUwKf3L0vSnGIRB4MA_r6trXHgBQlqy6ztiNHDfTtOurmo0-b-TJr_w; forterToken=32d5f233d1c648c98652263294a1bcd8_1733822399943_2958_UDF43-m4_21ck_; _ga_K8V0FL9E1N=GS1.1.1733822397.42.1.1733822410.0.0.0",
        "origin": "https://app.codatta.io",
        "priority": "u=1, i",
        "referer": "https://app.codatta.io/account/signin?from=%2Fapp%2Fquest%2FSUBCATE008",
        "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "signature": "9cda1622890db109c3d05aa2207e8f41",
        "timestamp": "1733822410542",
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMzkwNjI2NTM0MTA5MTg0IiwiY29ubmVjdG9yIjoid2FsbGV0IiwiYWNjb3VudF90eXBlIjoid2FsbGV0IiwiYWNjb3VudCI6IjB4YjQ3Zjc1YjFlYWFiOWE3MzJiNWZjNmQ5NjQ5ZGJkZjM2ZWY0ZDZjOCIsImxvZ2luX3NvdXJjZSI6ImNvZGF0dGEiLCJsb2dpbl93YWxsZXRfc291cmNlIjoiT0tYIFdhbGxldCJ9.ebqc0FlL8uROrCba6id3lENdR2JnWUUFVeecKfFdmKk",
        "uid": "390626534109184",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }
    # 发起POST请求
    response = requests.post(url, headers=headers)

    # 输出响应状态码和内容（根据实际需求调整输出方式）
    logging.info("Status Code: %s", response.status_code)
    logging.info("Response Content: %s", response.text)
import logging
from utils.crul_to_requests import curl_to_requests
from utils.api_assert import verify_response_structure
from utils.logger import log_execution


@log_execution
def test_select_reputation():
    curl_command = '''curl 'https://app.codatta.io/api/user/reputation/info' \
  -X 'POST' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: zh-CN,zh;q=0.9' \
  -H 'content-length: 0' \
  -H 'cookie: _ga=GA1.1.1344376451.1732246450; Codatta-Medical-WSI-Token=eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6ImNlNTlkYjYxLWEyY2EtNGJjNy05MTI0LWU1MTkxY2U2MGQ3MSJ9.4luKeMey_NK3UVXEclqxJ9THQIyw_pkoUwKf3L0vSnGIRB4MA_r6trXHgBQlqy6ztiNHDfTtOurmo0-b-TJr_w; forterToken=32d5f233d1c648c98652263294a1bcd8_1733984145744_2958_UDF43_21ck_; _ga_K8V0FL9E1N=GS1.1.1733984117.47.1.1733984147.0.0.0' \
  -H 'origin: https://app.codatta.io' \
  -H 'priority: u=1, i' \
  -H 'referer: https://app.codatta.io/app/reputation' \
  -H 'sec-ch-ua: "Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'signature: bbec39d3658def069f888a8fb3f49c5f' \
  -H 'timestamp: 1733984149581' \
  -H 'token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMzkwNjI2NTM0MTA5MTg0IiwiY29ubmVjdG9yIjoid2FsbGV0IiwiYWNjb3VudF90eXBlIjoid2FsbGV0IiwiYWNjb3VudCI6IjB4YjQ3Zjc1YjFlYWFiOWE3MzJiNWZjNmQ5NjQ5ZGJkZjM2ZWY0ZDZjOCIsImxvZ2luX3NvdXJjZSI6ImNvZGF0dGEiLCJsb2dpbl93YWxsZXRfc291cmNlIjoiT0tYIFdhbGxldCJ9.ebqc0FlL8uROrCba6id3lENdR2JnWUUFVeecKfFdmKk' \
  -H 'uid: 390626534109184' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36' '''
    
    logging.info("这是info接口，查询用户reputation")
    response = curl_to_requests(curl_command)
    verify_response_structure(response)

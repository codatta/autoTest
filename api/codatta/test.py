import requests

# 接口的基础URL
base_url = "http://example.com/api"
# 具体的接口端点，例如获取用户信息的接口
endpoint = "/users"
# 拼接完整的URL
url = base_url + endpoint

# 发起GET请求，可添加请求头（这里示例添加了一个自定义的头部，可按需修改）
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Authorization": "Bearer your_token_here"  # 如果接口需要认证，填入相应的token
}
response = requests.get(url, headers=headers)

# 查看响应状态码
print("响应状态码:", response.status_code)
# 查看响应内容（文本格式，通常用于返回HTML、JSON字符串等情况）
print("响应内容:", response.text)

# 如果响应内容是JSON格式，可以直接解析为Python字典
if response.headers.get('Content-Type') == 'application/json':
    data = response.json()
    print("解析后的JSON数据:", data)
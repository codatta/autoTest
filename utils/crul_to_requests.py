import logging
import re
import requests
from utils.logger import log_execution

@log_execution
def curl_to_requests(curl_command):
    """
    将curl命令转换为requests请求
    
    Args:
        curl_command: curl命令字符串
    Returns:
        requests的响应对象
    """
    logging.info("凡调用本方法的皆为接口函数")
    # 解析URL
    url_match = re.search(r"curl '([^']+)'", curl_command)
    if not url_match:
        url_match = re.search(r'curl "([^"]+)"', curl_command)
    if not url_match:
        raise ValueError("无法识别curl命令中的请求URL，请检查curl命令格式。")
    url = url_match.group(1)
    
    # 解析请求方法
    method_match = re.search(r"-X '([^']+)'", curl_command)
    method = method_match.group(1).upper() if method_match else 'GET'
    
    # 解析headers
    headers = {}
    header_matches = re.finditer(r"-H '([^:]+):([^']+)'", curl_command)
    for match in header_matches:
        key = match.group(1).strip()
        value = match.group(2).strip()
        headers[key] = value
        
    # 解析请求体数据（如果有）
    data = None
    data_match = re.search(r"-d '([^']+)'", curl_command)
    if data_match:
        data = data_match.group(1)
        
    # 发送请求
    if method == 'POST':
        response = requests.post(url, headers=headers, data=data)
    else:
        response = requests.get(url, headers=headers)
    return response
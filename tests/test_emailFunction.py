import logging

import pytest

from config.configBase import Config
from utils.my_email import send_email

# @pytest.mark.skip(reason="此测试用例暂时跳过，只用作测试邮箱功能")
def test_emailFunction():
    logging.info("这是测试邮件发送功能")
    # 邮件主题
    subject = "测试报告邮件"
    # 邮件正文内容
    body = "这是一封包含测试报告的邮件，请查收。"

    # 测试报告所在目录路径（假设你的测试报告在'reports'目录下，根据实际情况修改）
    report_directory =   Config.REPORT_PATH

    send_email(subject, body, Config.EMAIL_TOS, report_directory)
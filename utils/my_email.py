import logging
import os
import smtplib
import glob
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config.config_base import Config
from utils.logger import log_execution


@log_execution
def send_email(subject, body, to_emails, report_directory=None, *args, **kwargs):
    """
    发送邮件的函数。

    :param subject: 邮件主题。
    :param body: 邮件正文内容。
    :param to_emails: 收件人邮箱地址。
    :param report_directory: 测试报告所在的目录路径（可选），函数会将该目录下所有符合条件的报告文件作为附件发送。
    """
    # 发件人邮箱配置，这里使用配置文件中的设置，你需确保Config中有对应定义
    from_email = Config.EMAIL_FROM
    password = Config.EMAIL_PASSWORD

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = from_email
    # 将多个收件人地址用逗号连接后设置到邮件的 To 字段
    msg['To'] = ', '.join(to_emails)

    # 添加邮件正文
    msg.attach(MIMEText(body, 'plain'))

    # if report_directory:
    #     # 使用glob模块获取目录下所有.html格式的报告文件路径（可根据实际文件格式调整）
    #     report_paths = glob.glob(os.path.join(report_directory, "*.html"))
    #     for report_path in report_paths:
    #         with open(report_path, "rb") as f:
    #             part = MIMEApplication(f.read(), Name=os.path.basename(report_path))
    #         part['Content-Disposition'] = f'attachment; filename="{os.path.basename(report_path)}"'
    #         msg.attach(part)

    if report_directory:
        report_paths = glob.glob(os.path.join(report_directory, "*.html"))
        if len(report_paths) >= 2:  # 确保至少有两个报告
            # 按修改时间排序，获取第二新的报告
            report_paths.sort(key=os.path.getmtime, reverse=True)  # 从新到旧排序
            second_latest_report = report_paths[1]  # 获取第二新的报告
            with open(second_latest_report, "r", encoding='utf-8') as f:
                html_content = f.read()
            # 将 HTML 内容作为邮件正文
            msg.attach(MIMEText(html_content, 'html'))
            # 将 HTML 报告作为附件
            with open(second_latest_report, "rb") as f:
                part = MIMEApplication(f.read(), Name=os.path.basename(second_latest_report))
            part['Content-Disposition'] = f'attachment; filename="{os.path.basename(second_latest_report)}"'
            msg.attach(part)
        else :
            # 找到最新的 HTML 报告
            latest_report = max(report_paths, key=os.path.getmtime)
            with open(latest_report, "r", encoding='utf-8') as f:
                html_content = f.read()
            # 将 HTML 内容作为邮件正文
            msg.attach(MIMEText(html_content, 'html'))
            # 将 HTML 报告作为附件
            with open(latest_report, "rb") as f:
                part = MIMEApplication(f.read(), Name=os.path.basename(latest_report))
            part['Content-Disposition'] = f'attachment; filename="{os.path.basename(latest_report)}"'
            msg.attach(part)
    try:
        # 连接SMTP服务器并发送邮件，这里以常见的SMTP服务器为例，端口号587，使用TLS加密
        server = smtplib.SMTP(Config.SMTP_SERVER, Config.SMTP_PORT)
        server.starttls()
        server.login(from_email, password)
        # 循环遍历收件人列表发送邮件
        for to_email in to_emails:
            server.sendmail(from_email, to_email, msg.as_string())
            logging.info("已发送给：%s",to_email)
        server.quit()
    except smtplib.SMTPException as e:
        # 捕获SMTP相关的异常，比如连接失败、认证失败等
        logging.error(f"邮件发送失败，SMTP异常: {str(e)}")
    except FileNotFoundError as e:
        # 捕获可能出现的文件找不到的异常，比如附件文件不存在等情况
        logging.error(f"邮件发送失败，文件相关异常: {str(e)}")
    except Exception as e:
        # 捕获其他未预料到的异常情况
        logging.error(f"邮件发送失败，未知异常: {str(e)}")

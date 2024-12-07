import time
import pytest
from apscheduler.schedulers.background import BackgroundScheduler
from config.configBase import Config
from utils.baseFunction import delete_old_screenshots, delete_old_logs, delete_old_reports  # 导入删除报告的函数
from utils.my_email import send_email
from utils.logger import setup_logging


def run_tests():
    # 运行所有测试用例
    # 获取当前时间戳，用于区分不同轮次的测试报告文件名
    timestamp = time.strftime("%Y-%m-%d_%H-%M", time.localtime())
    report_file_path = Config.REPORT_PATH + f"/test_report_{timestamp}.html"
    # 运行所有测试用例，生成HTML报告并使用详细输出，使用动态生成的报告文件名
    result = pytest.main(["--html=" + report_file_path, "-s"])
    return result  # 返回结果以便后续处理


if __name__ == "__main__":
    logger = setup_logging()
    logger.info(".........这是一轮整体用例测试的开始.........")
    # 创建定时任务调度器
    scheduler = BackgroundScheduler()
    # 添加定时任务，这里设置为每天凌晨2点执行删除过期截图的任务，你可以根据需求调整触发时间
    scheduler.add_job(delete_old_screenshots, 'cron', hour=2, minute=0, args=[Config.SCREENPATH])
    # 添加定时任务，设置为每天凌晨3点执行删除过期日志的任务，可根据实际需求调整触发时间
    scheduler.add_job(delete_old_logs, 'cron', hour=3, minute=0, args=[Config.LOG_PATH])
    # 添加定时任务，设置为每天凌晨4点执行删除过期报告的任务，可根据需求调整触发时间
    scheduler.add_job(delete_old_reports, 'cron', hour=4, minute=0, args=[Config.REPORT_PATH])  # 添加删除报告定时任务
    # 添加定时任务，每天早上8点发送邮件（可根据实际需求调整时间和触发条件）
    scheduler.add_job(send_email, 'cron', hour=8, minute=0,
                      args=["每日测试情况汇报", "这是今日的测试相关情况汇报，请查看附件（也包含以往的报告，以文件名区分）。", Config.EMAIL_TOS,
                            Config.REPORT_PATH ])
    # 启动定时任务调度器
    scheduler.start()
    while True:
        exit_code = run_tests()  # 运行测试并获取退出代码
        time.sleep(1)
        if exit_code!= 0:
            print("有测试并未通过")  # 可以根据需要添加更多处理逻辑
        else:
            print("所有测试通过")
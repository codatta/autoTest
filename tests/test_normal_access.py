import logging
import time
from datetime import datetime
from config.configBase import Config
from utils.baseFunction import  clickbyText, findText


def test_normal_access(setup_driver):
    logging.info("这是测试referral界面copy按钮是否可以点击")

    timestart = datetime.now()  # 记录开始时间
    driver = setup_driver
    driver.get('https://' + Config.DOMAIN + '/app/referral')
    time.sleep(5)
    clickbyText(driver,"Copy Link")
    findText(driver,"copied")
    timeend = datetime.now()
    logging.info(timeend - timestart)
    logging.info("test_normal_access over.................")
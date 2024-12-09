
import logging
import time
from datetime import datetime
from config.configBase import Config
from utils.baseFunction import  clickbyText, findText


def test_access_quest(setup_driver):
    timestart = datetime.now()  # 记录开始时间
    driver = setup_driver
    driver.get('https://' + Config.DOMAIN + '/app/quest/SUBCATE002')
    time.sleep(5)
    findText(driver,"Successfully complete")
    timeend = datetime.now()
    logging.info(timeend - timestart)
    logging.info("test_normal_access over.................")
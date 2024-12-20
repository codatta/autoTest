
import logging
import time
from datetime import datetime
from config.config_base import Config
from utils.base_function import  clickbyText, findText

def test_access_quest(setup_driver):
    logging.info("这是访问界面中的SUBCATE002任务用例")
    timestart = datetime.now()  # 记录开始时间
    driver = setup_driver
    driver.get('https://' + Config.DOMAIN + '/app/quest/SUBCATE002')
    time.sleep(5)
    findText(driver,"Successfully complete")
    timeend = datetime.now()
    logging.info(timeend - timestart)
    logging.info("test_access_quest over.................")
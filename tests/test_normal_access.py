import logging
import time
from datetime import datetime
from config.configBase import Config
from utils.baseFunction import find_text_on_page, clickbyText


def test_normal_access(setup_driver):
    timestart = datetime.now()  # 记录开始时间
    driver = setup_driver
    driver.get('https://' + Config.DOMAIN + '/app')
    clickbyText(driver,"referral")
    find_text_on_page(driver,"copy")
    times = datetime.now() - timestart  # 记录开始时间
    logging.info("time is: " + str(times))
    driver.quit()
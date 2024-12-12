import logging
import time
from datetime import datetime
from config.config_base import Config
from utils.base_function import clickbyText, findText

def test_copy_link(setup_driver):
    """
    测试referral界面copy按钮功能
    
    Args:
        setup_driver: pytest fixture，提供配置好的WebDriver实例
    """
    logging.info("这是测试referral界面copy按钮是否可以点击")
    logging.info("测试步骤：点击Copy Link")
    logging.info("测试步骤：查找copied")

    timestart = datetime.now()
    driver = setup_driver
    
    try:
        driver.get('https://' + Config.DOMAIN + '/app/referral')
        time.sleep(5)
        clickbyText(driver, "Copy Link")
        findText(driver, "copied")
        
        timeend = datetime.now()
        logging.info(timeend - timestart)
        logging.info("test_copy_link over.................")
    except Exception as e:
        logging.error(f"测试过程中发生错误: {str(e)}")

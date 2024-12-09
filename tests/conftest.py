import logging
import pytest

from config.configBase import Config
from utils.configBase import init



@pytest.fixture(scope='session', autouse=True)
def setup_driver():
    driver = None
    try:
        logger = logging.getLogger()
        logger.info(".........夹具开始执行.........")
        driver = init()
        yield driver
        logger.info(".........夹具结束执行，开始清理工作.........")
        driver.quit()
    except Exception as e:
        print("出现错误重新开始")
        Config.MISTAKECOUNT +=1
        print("失败次数", Config.MISTAKECOUNT)
        print(e)



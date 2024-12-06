import pytest
from config.configBase import Config
from utils.configBase import init

@pytest.fixture(scope='session', autouse=True)
def setup_driver():

    driver = None
    try:
        driver = init()
        yield driver
    except Exception as e:
        print("出现错误重新开始")
        mistakecount = Config.MISTAKECOUNT + 1
        print("失败次数", mistakecount)
        print(e)
    finally:
        if driver is not None:
            driver.quit()
            print("退出网页")

import logging
from datetime import datetime
import time
from selenium.webdriver.common.by import By
from utils.baseFunction import slidePage, upload, screenshot, clickbyText, findText
from config.configBase import  Config
from selenium.webdriver.common.keys import Keys




def test_submission(setup_driver):
    """
    测试提交功能的测试用例。

    该测试用例模拟用户在网页上进行提交操作的过程，包括输入网络、地址和哈希值，
    并上传文件。测试完成后，刷新页面并返回操作计数。

    :param driver: Selenium WebDriver 实例，用于与浏览器进行交互。
    :return: 更新后的操作计数。
    """
    timestart = datetime.now()  # 记录开始时间
    driver=setup_driver
    driver.get('https://' + Config.DOMAIN + '/app/submission/submit?category=personal-data')
    time.sleep(5)
    driver.execute_script("window.open('https://manta.dex.guru/', '_blank');")
    # 输入网络
    time.sleep(8)  # 等待页面加载
    input = driver.find_element(By.ID, 'network')
    input.send_keys('manta')
    input.send_keys(Keys.ENTER)
    time.sleep(2)
    # 打开新窗口

    driver.switch_to.window(driver.window_handles[1])
    time.sleep(5)
    screenshotpath1 = screenshot(driver, choice=1)
    # 点击第一个元素的具体交易然后截图
    button = driver.find_element(By.XPATH,
                                 ' /html/body/div/div/div/div[2]/div[3]/div[2]/div[2]/div/table/tbody/tr[1]/td[1]/div/div[2]/strong/span/a')
    button.click()
    time.sleep(2)
    screenshotpath2 = screenshot(driver, choice=2)
    time.sleep(2)
    driver.back()
    time.sleep(2)
    # 点击第一个元素
    button = driver.find_element(By.XPATH,
                                 '/html/body/div/div/div/div[2]/div[3]/div[2]/div[2]/div/table/tbody/tr[1]/td[2]/div/div[1]/span/button/span')
    button.click()
    time.sleep(2)
    # 切换回第一个窗口
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)
    # 输入地址

    input = driver.find_element(By.ID, 'address')

    # 粘贴地址
    input.send_keys(Keys.COMMAND, 'v')
    time.sleep(2)
    # 切换到新窗口,复制hash
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
    button = driver.find_element(By.XPATH,
                                 '/html/body/div/div/div/div[2]/div[3]/div[2]/div[2]/div/table/tbody/tr[1]/td[1]/div/div[2]/strong/span/button/span')
    button.click()
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)
    slidePage(driver, '下', 1000)
    # 粘贴hash
    input = driver.find_element(By.ID, 'evidence_hash')

    input.send_keys(Keys.COMMAND, 'v')

    input = driver.find_element(By.ID, 'evidence_text')

    input.send_keys(Keys.COMMAND, 'v')
    # 选择类别
    input = driver.find_element(By.ID, 'category')

    input.click()
    input.send_keys('Cold')
    clickbyText(driver, "Wallet and Storage",Config.IMPLICIT_WAIT_TIME)
    # 选择类别
    clickbyText(driver, "Category",Config.IMPLICIT_WAIT_TIME)
    time.sleep(2)

    button = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[2]/div/main/div/div[2]/div[1]/form/div[2]/div[4]/div/div[2]/div/div/div/span/div/span')
    time.sleep(1)
    upload(driver, screenshotpath1, 'XPATH',
           '/html/body/div[1]/div[2]/div/main/div/div[2]/div[1]/form/div[2]/div[4]/div/div[2]/div/div/div/span/div/span/input')
    time.sleep(3)
    upload(driver, screenshotpath2, 'XPATH',
           '/html/body/div[1]/div[2]/div/main/div/div[2]/div[1]/form/div[2]/div[4]/div/div[2]/div/div/div/span/div/span/input')
    time.sleep(3)

    slidePage(driver, '下', 1000)

    button = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[2]/div/main/div/div[2]/div[1]/form/button')
    button.click()
    logging.info("点击submit")
    time.sleep(8)
    findText(driver,"successful")
    driver.refresh()
    logging.info("刷新")
    time.sleep(2)
    timeend = datetime.now()
    logging.info(timeend - timestart)
    logging.info("test_submission over.................")
    return   # 返回操作计数
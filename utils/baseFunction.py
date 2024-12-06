# 可以在这里进行其他操作，如提取信息、点击按钮等
import logging
from datetime import  datetime
import os
import time
import glob
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re

from config.configBase import Config
from utils.logger import log_execution


@log_execution
def clickbyText(driver, text, timeout=Config.IMPLICIT_WAIT_TIME, exception=True, fuzzy=True):
    """
    根据给定的文本点击页面元素，支持模糊匹配。

    :param driver: Selenium WebDriver 实例，用于与浏览器交互。
    :param text: 要查找的元素文本。
    :param timeout: 等待元素可点击的超时时间（秒），默认为配置中的隐式等待时间。
    :param exception: 是否捕获异常，默认为 True。
    :param fuzzy: 是否启用模糊匹配，默认为 False。
    """
    if exception:
        try:
            # 等待指定的时间，直到页面中加载所有元素
            WebDriverWait(driver, timeout).until(
                EC.presence_of_all_elements_located((By.XPATH, "//*"))
            )
            
            # 获取页面的所有元素
            elements = driver.find_elements(By.XPATH, "//*")
            for element in elements:
                element_text = element.text
                if fuzzy:
                    # 使用正则表达式进行模糊匹配
                    pattern = re.compile(re.escape(text), re.IGNORECASE)  # 忽略大小写
                    if pattern.search(element_text):
                        element.click()
                        print(f"成功点击包含模糊匹配文字 '{text}' 的元素")
                        return
                else:
                    # 精确匹配
                    if element_text == text:
                        element.click()
                        print(f"成功点击包含文字 '{text}' 的元素")
                        return
            
            print(f"未找到包含文字 '{text}' 的元素")
        except Exception as e:
            print(f"查找或点击元素时发生错误")
    else:
        # 不捕获异常的情况
        WebDriverWait(driver, timeout).until(
            EC.presence_of_all_elements_located((By.XPATH, "//*"))
        )
        
        # 获取页面的所有元素
        elements = driver.find_elements(By.XPATH, "//*")
        for element in elements:
            element_text = element.text
            if fuzzy:
                # 使用正则表达式进行模糊匹配
                pattern = re.compile(re.escape(text), re.IGNORECASE)  # 忽略大小写
                if pattern.search(element_text):
                    element.click()
                    print(f"成功点击包含模糊匹配文字 '{text}' 的元素")
                    return
            else:
                # 精确匹配
                if element_text == text:
                    element.click()
                    print(f"成功点击包含文字 '{text}' 的元素")
                    return
        
        print(f"未找到包含文字 '{text}' 的元素")

# 滑动页面
@log_execution
def slidePage(driver, direction='下', distance=100, exception=True):
    """
    滑动页面到指定方向。

    :param driver: Selenium WebDriver 实例，用于与浏览器交互。
    :param direction: 滑动方向，支持 '上'、'下'、'左'、'右'。
    :param distance: 滑动的距离（像素），默认为 100。
    :param exception: 是否捕获异常，默认为 True。
    """
    if exception:
        try:
            if direction == '下':
                if distance:
                    # 使用 JavaScript 滑动指定距离
                    driver.execute_script(f"window.scrollBy(0, {distance});")
                else:
                    # 滑动到页面底部
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            elif direction == '上':
                if distance:
                    driver.execute_script(f"window.scrollBy(0, -{distance});")
                else:
                    # 滑动到页面顶部
                    driver.execute_script("window.scrollTo(0, 0);")
            elif direction == '右':
                driver.execute_script(f"window.scrollBy({distance}, 0);")
            elif direction == '左':
                driver.execute_script(f"window.scrollBy(-{distance}, 0);")
            print(f"已{direction}滑动页面")
        except:
            print("滑动页面失败")
    else:
        if direction == '下':
            if distance:
                # 使用 JavaScript 滑动指定距离
                driver.execute_script(f"window.scrollBy(0, {distance});")
            else:
                # 滑动到页面底部
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        elif direction == '上':
            if distance:
                driver.execute_script(f"window.scrollBy(0, -{distance});")
            else:
                # 滑动到页面顶部
                driver.execute_script("window.scrollTo(0, 0);")
        elif direction == '右':
            driver.execute_script(f"window.scrollBy({distance}, 0);")
        elif direction == '左':
            driver.execute_script(f"window.scrollBy(-{distance}, 0);")
        print(f"已{direction}滑动页面")

# 上传文件
@log_execution
def upload(driver, filepath, xpath='name', xpathname='file',exception=True):
    if exception:
        try:
            # 确保文件路径是绝对路径
            completepath = os.path.abspath(filepath)

            # 找到文件输入元素
            fileinput = driver.find_element(getattr(By, xpath.upper()), xpathname)

            # 直接发送文件路径到输入元素
            fileinput.send_keys(completepath)

            print(f"已成功上传文件：{completepath}")
        except Exception as e:
            print(f"文上传失败：{str(e)}")
    else:
        # 确保文件路径是绝对路径
        completepath = os.path.abspath(filepath)

        # 找到文件输入元素
        fileinput = driver.find_element(getattr(By, xpath.upper()), xpathname)

        # 直到发送文件路径到输入元素
        fileinput.send_keys(completepath)

        print(f"已成功上传文件：{completepath}")


# 截取浏览器界面
@log_execution
def screenshot(driver, savePath=None, choice=1):
    try:
        # 获取当前日期和时间
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # 格式化为 "YYYY-MM-DD_HH-MM-SS"
        
        # 如果没有指定保存路径，则使用默认路径和文件名
        if not savePath:
            if choice == 1:
                savePath = os.path.join(Config.SCREENPATH, f"screenshot_{current_time}_3000.png")
            else:
                savePath = os.path.join(Config.SCREENPATH, f"screenshot_{current_time}_4000.png")
        else:
            if choice == 1:
                savePath = os.path.join(Config.SCREENPATH + savePath, f"screenshot_{current_time}_3000.png")
            else:
                savePath = os.path.join(Config.SCREENPATH + savePath, f"screenshot_{current_time}_4000.png")
        
        # 截取整个页面
        screen = driver.get_screenshot_as_png()
        time.sleep(2)
        # 保存截图
        with open(savePath, "wb") as file:
            file.write(screen)
        time.sleep(2)
        print(f"截图已保存至：{savePath}")
        # 删除超过7天的截图
        delete_old_screenshots(Config.SCREENPATH, days=7)
        file.close()
        return savePath
    except Exception as e:
        print(f"截图失败：{str(e)}")
        file.close()
        return None
def delete_old_screenshots(directory, days=7):
    """
    删除指定目录中超过指定天数的截图文件。

    :param directory: 存放截图的目录
    :param days: 超过多少天的文件将被删除
    """
    # 获取当前时间
    current_time = time.time()
    # 计算过期时间
    expiration_time = current_time - (days * 86400)  # 86400秒 = 1天

    # 查找所有截图文件
    for file in glob.glob(os.path.join(directory, "screenshot_*.png")):
        # 获取文件的最后修改时间
        logging.info(os.path.abspath(file))
        file_mod_time = os.path.getmtime(file)
        logging.info("............"+file_mod_time)
        # 如果文件过期，则删除
        if file_mod_time < expiration_time:
            os.remove(file)
            print(f"已删除过期截图：{file}")
            
@log_execution
def find_text_on_page(driver, text, timeout=Config.IMPLICIT_WAIT_TIME, exception=True, fuzzy=True):
    """
    查找页面中是否包含指定的文本，支持模糊匹配。

    :param driver: Selenium WebDriver 实例，用于与浏览器交互。
    :param text: 要查找的文本字符串��
    :param timeout: 等待文本出现的最大时间（秒），默认为配置中的隐式等待时间。
    :param exception: 是否捕获异常，默认为 True。
    :param fuzzy: 是否启用模糊匹配，默认为 False。
    :return: 如果找到文本，返回 True；否则返回 False。
    """
    if exception:
        try:
            # 等待页面加载完成，直到页面中所有元素可见
            WebDriverWait(driver, timeout).until(
                EC.visibility_of_all_elements_located((By.XPATH, "//*"))
            )
            
            # 获取页面的所有元素
            elements = driver.find_elements(By.XPATH, "//*")
            all_text = " ".join([element.text for element in elements])  # 获取所有元素的文本
            
            print(f"页面文本内容: {all_text}")  # 打印页面的完整文本内容
            
            if fuzzy:
                # 使用正则表达式进行模糊匹配
                pattern = re.compile(re.escape(text), re.IGNORECASE)  # 忽略大小写
                if pattern.search(all_text):
                    print(f"成功找到模糊匹配文本：'{text}'")
                    return True
            else:
                # 精确匹配
                if text in all_text:
                    print(f"成功找到��本：'{text}'")
                    return True
            
            print(f"未找到文本：'{text}'")
            return False
        except Exception as e:
            # 如果在超时时间内未找到文本，打印错误信息
            print(f"查找文本时发生错误")
            return False
    else:
        # 不捕获异常的情况
        WebDriverWait(driver, timeout).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//*"))
        )
        
        # 获取页面的所有元素
        elements = driver.find_elements(By.XPATH, "//*")
        all_text = " ".join([element.text for element in elements])  # 获取所有元素的文本
        
        print(f"页面文本内容: {all_text}")  # 打印页面的完整文本内容
        
        if fuzzy:
            # 使用正则表达式进行模糊匹配
            pattern = re.compile(re.escape(text), re.IGNORECASE)  # 忽略大小写
            if pattern.search(all_text):
                print(f"成功找到模糊匹配文本：'{text}'")
                return True
        else:
            # 精确匹配
            if text in all_text:
                print(f"成功找到文本：'{text}'")
                return True
        
        print(f"未找到文本：'{text}'")
        return False
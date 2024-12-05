# 可以在这里进行其他操作，如提取信息、点击按钮等
import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from config.configBase import Config


def clickbyText(driver, text, timeout=10, exception=True):
    """
    根据给定的文本点击元素。

    :param driver: Selenium WebDriver实例
    :param text: 要查找的元素文本
    :param timeout: 等待元素可点击的超时时间（秒）
    :param exception: 是否捕获异常，默认为True
    """
    if exception:
        try:
            xpath = f"//*[contains(text(), '{text}')]"
            element = WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            element.click()
            time.sleep(2)
            print(f"成功点击包含文字 '{text}' 的元素")
        except:
            print(f"未找到或无法点击包含文字 '{text}' 的元素")
    else:
        xpath = f"//*[contains(text(), '{text}')]"
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        element.click()
        time.sleep(2)
        print(f"成功点击包含文字 '{text}' 的元素")
        # 不再捕获异常
   

# 滑动页面
def slidePage(driver, direction='下', distance=100,exception=True):
    if exception:
        try:
            if direction == '下':
                if distance:
                    # 使用JavaScript滑动指定distance
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
                # 使用JavaScript滑动指定distance
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
            print(f"文件上传失败：{str(e)}")
    else:
        # 确保文件路径是绝对路径
        completepath = os.path.abspath(filepath)

        # 找到文件输入元素
        fileinput = driver.find_element(getattr(By, xpath.upper()), xpathname)

        # 直接发送文件路径到输入元素
        fileinput.send_keys(completepath)

        print(f"已成功上传文件：{completepath}")


# 截取浏览器界面
def screenshot(driver, savePath=None, choice=1):
    try:
        # 如果没有指定保存路径，则使用默认路径和文件名
        if not savePath:
            if choice == 1:
                savePath = os.path.join(Config.SCREENPATH, "3000.png")
            else:
                savePath = os.path.join(Config.SCREENPATH, "4000.png")
        else:
            if choice == 1:
                savePath = os.path.join(Config.SCREENPATH+savePath, "3000.png")
            else:
                savePath = os.path.join(Config.SCREENPATH+savePath, "4000.png")
        # 截取整个页面
        screen = driver.get_screenshot_as_png()
        time.sleep(2)
        # 保存截图
        with open(savePath, "wb") as file:
            file.write(screen)
        time.sleep(2)
        print(f"截图已保存至：{savePath}")
        file.close()
        return savePath
    except Exception as e:
        print(f"截图失败：{str(e)}")
        file.close()
        return None

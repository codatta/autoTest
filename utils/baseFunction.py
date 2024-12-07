# 可以在这里进行其他操作，如提取信息、点击按钮等
import logging
from datetime import  datetime, timedelta
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
def clickbyText(driver, text, timeout=Config.IMPLICIT_WAIT_TIME, exception=True, fuzzy=True, partial_match=True,*args, **kwargs):
    """
    根据给定的文本点击页面元素，支持模糊匹配、精确匹配以及部分匹配等多种方式。

    :param driver: Selenium WebDriver实例，用于与浏览器交互。
    :param text: 要查找的元素文本。
    :param timeout: 等待元素可点击的超时时间（秒），默认为配置中的隐式等待时间。
    :param exception: 是否捕获异常并记录详细错误信息，默认为True。
    :param fuzzy: 是否启用模糊匹配（包含文本即可），默认为True。
    :param partial_match: 是否启用部分匹配（文本是元素文本的一部分），默认为True。
    """
    logging.info(f"要点击的文字是：{text}")
    try:
        # 等待页面加载完成，这里使用更灵活的等待元素可点击的条件，而不仅仅是将元素存在作为等待条件
        WebDriverWait(driver, timeout).until(
            EC.presence_of_all_elements_located((By.XPATH, "//*"))
        )

        if fuzzy:
            if partial_match:
                # 模糊且部分匹配，忽略大小写，去除文本两端空白后进行匹配
                xpath_expr = f"//*[contains(translate(normalize-space(text()), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{text.strip().lower()}')]"
            else:
                # 模糊匹配，文本完整出现（忽略大小写），去除文本两端空白后进行匹配
                xpath_expr = f"//*[normalize-space(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')) = '{text.strip().lower()}']"
            elements = driver.find_elements(By.XPATH, xpath_expr)
            assert elements is not None, f"模糊匹配查找元素，预期能找到元素，但实际返回None，文本为 {text}"
            if elements:
                found_clickable = False
                # 找到多个匹配元素时，优先点击可见且可点击的元素
                for element in elements:
                    if element.is_displayed() and element.is_enabled():
                        element.click()
                        logging.info(f"成功点击包含模糊匹配文字 '{text}' 的元素")
                        assert True, f"成功点击包含模糊匹配文字 '{text}' 的元素"
                        found_clickable = True
                        return
                if not found_clickable:
                    logging.warning(f"找到包含模糊匹配文字 '{text}' 的多个元素，但均不可点击或不可见，无法完成点击操作")
            else:
                logging.warning(f"未找到包含模糊匹配文字 '{text}' 的元素")
        else:
            # 精确匹配
            xpath_expr = f"//*[normalize-space(text()) = '{text.strip()}']"
            element = driver.find_element(By.XPATH, xpath_expr)
            assert element is not None, f"精确匹配查找元素，预期能找到元素，但实际返回None，文本为 {text}"
            if element.is_displayed() and element.is_enabled():
                element.click()
                logging.info(f"成功点击包含文字 '{text}' 的元素")
                assert True, f"成功点击包含文字 '{text}' 的元素"
                return
            else:
                logging.warning(f"找到包含文字 '{text}' 的元素，但不可点击或不可见，无法完成点击操作")
    except Exception as e:
        if exception:
            logging.error(f"查找或点击元素时发生错误，详细信息: {str(e)}", exc_info=True)
            raise e
        else:
            logging.warning(f"查找或点击元素时发生错误，但不抛出异常，错误信息: {str(e)}")
    return  # 无论是否出现异常，只要exception为False，就直接返回，保证测试用例继续执行

# 滑动页面
@log_execution
def slidePage(driver, direction='下', distance=100, exception=True, *args, **kwargs):
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
            logging.info(f"已{direction}滑动页面")
        except:
            logging.info("滑动页面失败")
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
        logging.info(f"已{direction}滑动页面")

# 上传文件
@log_execution
def upload(driver, filepath, xpath='name', xpathname='file', exception=True, *args, **kwargs):
    """
    用于实现文件上传功能，通过定位页面中的文件输入元素并发送文件路径来完成上传操作。

    :param driver: Selenium WebDriver实例，用于与浏览器交互。
    :param filepath: 要上传文件的路径，函数内部会将其转换为绝对路径。
    :param xpath: 定位文件输入元素的方式，默认是 'name'，可根据实际情况选择如'id'、'xpath'等，会转换为对应的By类属性。
    :param xpathname: 文件输入元素在对应定位方式下的名称或表达式，用于精准定位元素。
    :param exception: 是否捕获异常并记录详细错误信息，默认为True，若为False则只记录简单错误信息不抛出异常中断流程。
    """
    try:
        # 确保文件路径是绝对路径
        completepath = os.path.abspath(filepath)
        assert os.path.exists(completepath), f"指定的文件路径 {completepath} 不存在，请检查文件路径是否正确"

        # 找到文件输入元素
        fileinput = driver.find_element(getattr(By, xpath.upper()), xpathname)
        assert fileinput is not None, f"未能找到指定的文件输入元素，定位方式为 {xpath}，名称或表达式为 {xpathname}"

        # 直接发送文件路径到输入元素
        fileinput.send_keys(completepath)
        assert True, f"已成功将文件路径 {completepath} 发送到文件输入元素，理论上已触发上传流程"

        logging.info(f"已成功上传文件：{completepath}")
    except Exception as e:
        if exception:
            logging.error(f"文件上传失败：{str(e)}", exc_info=True)
            raise e
        else:
            logging.warning(f"文件上传出现问题，但不抛出异常，错误信息: {str(e)}")

# 截取浏览器界面
@log_execution
def screenshot(driver, savePath=None, choice=1, *args, **kwargs):
    try:
        # 获取当前日期和时间
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M")  # 格式化为 "YYYY-MM-DD_HH-MM-SS"
        
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
        dir_name = os.path.dirname(savePath)
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        with open(savePath, "wb") as file:
            file.write(screen)
        time.sleep(2)
        logging.info(f"截图已保存至：{savePath}")
        return savePath
    except Exception as e:
        logging.info(f"截图失败：{str(e)}")
        return None

@log_execution
def delete_old_screenshots(directory, days=Config.EXPIRATION_TIME_SCREENSHOT, *args, **kwargs):
    """
    删除指定目录中超过指定天数的截图文件。

    :param directory: 存放截图的目录
    :param days: 超过多少天的文件将被删除
    """
    # 检查目录是否存在
    if not os.path.exists(directory):
        logging.warning(f"目录不存在: {directory}")
        return
    # 获取当前时间
    current_time = datetime.now()
    # 计算过期时间
    expiration_time = current_time - timedelta(days=days)  # 计算过期时间

    # 查找所有截图文件
    for file in glob.glob(os.path.join(directory, "screenshot_*.png")):
        try:
            # 从文件名中提取日期
            filename = os.path.basename(file)
            date_str = filename.split('_')[1]  # 假设文件名格式为 screenshot_YYYY-MM-DD_XXXX.png
            file_date = datetime.strptime(date_str, "%Y-%m-%d")  # 将字符串转换为日期对象
            
            # 如果文件日期早于过期时间，则删除
            if file_date < expiration_time:
                os.remove(file)
                logging.info(f"已删除过期截图：{file}")
        except Exception as e:
            logging.error(f"删除文件时发生错误: {file}, 错误信息: {str(e)}")

@log_execution
def delete_old_logs(directory, days=Config.EXPIRATION_TIME_LOG, *args, **kwargs):
    """
    删除指定目录中超过指定天数的日志文件。

    :param directory: 存放日志文件的目录
    :param days: 超过多少天的文件将被删除
    """
    # 检查目录是否存在
    if not os.path.exists(directory):
        logging.warning(f"目录不存在: {directory}")
        return
    # 获取当前时间
    current_time = datetime.now()
    # 计算过期时间
    expiration_time = current_time - timedelta(days=days)  # 计算过期时间

    # 查找所有日志文件，这里假设日志文件格式为log_YYYY-MM-DD.log，可根据实际调整
    for file in glob.glob(os.path.join(directory, "log_*.log")):
        try:
            # 从文件名中提取日期
            filename = os.path.basename(file)
            date_str = filename.split('_')[1].split('.')[0]  # 获取文件名中日期部分并去掉.log后缀
            file_date = datetime.strptime(date_str, "%Y-%m-%d")  # 将字符串转换为日期对象

            # 如果文件日期早于过期时间，则删除
            if file_date < expiration_time:
                os.remove(file)
                logging.info(f"已删除过期日志：{file}")
        except Exception as e:
            logging.error(f"删除文件时发生错误: {file}, 错误信息: {str(e)}")

@log_execution
def delete_old_reports(directory, days=Config.EXPIRATION_TIME_REPORTS):
    """
    删除指定目录中超过指定天数的测试报告文件。

    :param directory: 存放测试报告文件的目录
    :param days: 超过多少天的文件将被删除
    """
    # 检查目录是否存在
    if not os.path.exists(directory):
        logging.warning(f"目录不存在: {directory}")
        return
    # 获取当前时间
    current_time = datetime.now()
    # 计算过期时间
    expiration_time = current_time - timedelta(days=days)

    for file in glob.glob(os.path.join(directory, "test_report_*.html")):
        try:
            # 从文件名中提取日期
            filename = os.path.basename(file)
            date_str = filename.split('_')[2].split('.')[0]
            file_date = datetime.strptime(date_str, "%Y-%m-%d")

            # 如果文件日期早于过期时间，则删除
            if file_date < expiration_time:
                os.remove(file)
                logging.info(f"已删除过期报告：{file}")
        except Exception as e:
            logging.error(f"删除文件时发生错误: {file}, 错误信息: {str(e)}")
@log_execution
def find_text_on_page(driver, text, timeout=Config.IMPLICIT_WAIT_TIME, exception=True, fuzzy=True, *args, **kwargs):
    """
    查找页面中是否包含指定的文本，支持模糊匹配。

    :param driver: Selenium WebDriver实例，用于与浏览器交互。
    :param text: 要查找的文本字符串。
    :param timeout: 等待文本出现的最大时间（秒），默认为配置中的隐式等待时间。
    :param exception: 是否捕获异常，默认为True。
    :param fuzzy: 是否启用模糊匹配，默认为False。
    :return: 如果找到文本，返回True；否则返回False。
    """
    try:
        # 等待页面加载完成，直到页面中所有元素可见
        WebDriverWait(driver, timeout).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//*"))
        )
        assert driver.current_url, "页面加载完成后，当前URL不应为空，可能页面加载出现问题"

        # 获取页面的所有元素
        elements = driver.find_elements(By.XPATH, "//*")
        assert elements, "未能获取到页面的任何元素，可能元素查找出现问题"

        all_text = " ".join([element.text for element in elements])  # 获取所有元素的文本

        logging.info(f"页面文本内容: {all_text}")  # 打印页面的完整文本内容

        if fuzzy:
            # 使用正则表达式进行模糊匹配
            pattern = re.compile(re.escape(text), re.IGNORECASE)  # 忽略大小写
            assert pattern, "正则表达式编译失败，可能正则表达式语法有误"
            if pattern.search(all_text):
                logging.info(f"成功找到模糊匹配文本：'{text}'")
                assert True, f"成功找到模糊匹配文本 '{text}'，符合预期"
                return True
        else:
            # 精确匹配
            assert text, "要进行精确匹配的文本不能为空，否则无法进行匹配"
            if text in all_text:
                logging.info(f"成功找到文本：'{text}'")
                assert True, f"成功找到文本 '{text}'，符合预期"
                return True

        logging.info(f"未找到文本：'{text}'")
        assert False, f"未找到预期文本 '{text}'，不符合预期"
    except Exception as e:
        if exception:
            logging.error(f"查找文本时发生错误，详细信息: {str(e)}", exc_info=True)
            raise e
        else:
            logging.warning(f"查找文本时发生错误，但不抛出异常，错误信息: {str(e)}")
            return False
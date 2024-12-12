import logging
import os
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler


from config.config_base import Config

def setup_logging(log_directory=Config.LOGS, backup_count=400, interval=30):
    """
    设置日志记录。

    :param log_directory: 日志文件存储目录。
    :param backup_count: 保留的旧日志文件数量。
    :param interval: 轮换间隔（分钟）。
    """
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    # 生成日志文件名
    current_time = datetime.now().strftime("%Y-%m-%d_%H_%M")
    log_file_name = f"log_{current_time}.log"

    # 创建文件处理器
    file_handler = TimedRotatingFileHandler(
        os.path.join(log_directory, log_file_name),
        when='M',  # 每分钟轮换
        interval=interval,
        backupCount=backup_count
    )

    # 设置日志格式
    file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)

    # # 创建控制台处理器
    # console_handler = logging.StreamHandler()
    # console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    # console_handler.setFormatter(console_formatter)

    # 获取根日志记录器并设置级别
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  # 设置日志级别
    logger.addHandler(file_handler)  # 添加文件处理器
    # logger.addHandler(console_handler)  # 添加控制台处理器

    return logger

def log_execution(func):
    """
    装饰器，用于记录函数的执行情况。
    只能用于函数，不可用于用例否则会出现错误
    :param func: 被装饰的函数。
    :return: 包装后的函数。
    """
    def wrapper(*args, **kwargs):
        try:
            logging.info(f"............开始执行函数: {func.__name__}，参数: {args}, 关键字参数: {kwargs}............")
            result = func(*args, **kwargs)
            logging.info(f"............完成执行函数: {func.__name__},返回: {result}............")
            return result
        except Exception as e:
            logging.error(f"............执行函数时发生错误............")
            raise  # 重新抛出异常
    return wrapper


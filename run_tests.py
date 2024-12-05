import time
import pytest
from config.configBase import Config

def run_tests():
    # 运行所有测试用例
    result = pytest.main(["--html=" + Config.REPORT_PATH, "-v"])  # 生成 HTML 报告并使用详细输出
    return result  # 返回结果以便后续处理

if __name__ == "__main__":
    while True:
        exit_code = run_tests()  # 运行测试并获取退出代码
        time.sleep(100)
        if exit_code != 0:
            print("有测试并未通过")  # 可以根据需要添加更多处理逻辑
        else:
            print("所有测试通过")

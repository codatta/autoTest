# 自动化测试 Codatta 项目

这是用于自动化测试 Codatta 的项目。该项目旨在提供一个灵活的测试框架，以便于对 Codatta 进行全面的自动化测试。

## 项目状态

- **框架尚未搭建完成，已完成部分**

    - 日志循环保存和定时删除
    - 报告做了循环保存和定时删除和定时发送到邮件
    - 发送邮件功能已完成，可以群发，定时发送，会发送所有的报告
    - 基础工具类断言等并未完成
    - 用例目前只有两个
    - 图片做了过期删除
    - 还没有做只选定部分用例执行功能
  
## 功能特性

- **自动化测试**: 提供基本的自动化测试功能。
- **日志记录**: 记录测试过程中的重要信息和错误。
- **报告生成**: 生成测试报告以便于查看测试结果。

## 安装

请确保您已安装 Python 3.x 和 pip。然后，您可以通过以下命令安装项目依赖：

**pip install -r requirements.txt**

## 使用

1. 克隆项目到本地：

    ```bash
    git clone <your-repo-url>
    cd autoTestProjecte
    ```

2. 运行测试用例：

    ```bash
    python runtests.txt
    ```

## 贡献

欢迎任何形式的贡献！如果您有建议或想要修复某个问题，请提交问题或拉取请求。

## 许可证

本项目采用 MIT 许可证，详细信息请参见 [LICENSE](LICENSE) 文件。
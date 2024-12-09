# 使用基于Debian的基础镜像（也可以选择其他合适的基础镜像）
FROM debian:latest

# 更新软件源列表
RUN apt-get update

# 安装必要的依赖，这些依赖是运行谷歌浏览器和ChromeDriver所需要的
RUN apt-get install -y wget gnupg2 ca-certificates fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgbm1 libgcc1 libglib2.0-0 libgtk-3-0 libnspr4 libnss3 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 lsb-release xdg-utils

# 下载并安装谷歌浏览器
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb || apt-get install -f -y

# 下载并安装ChromeDriver（这里假设下载特定版本，你可以根据实际需求替换版本号）
RUN wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip
RUN mv chromedriver /usr/local/bin/
RUN chmod +x /usr/local/bin/chromedriver

# 设置工作目录（可选，根据你的实际使用情况调整）
WORKDIR /app

# 可以将你的自动化测试代码复制到容器内（假设你的代码在本地当前目录下名为test.py，以下是示例，按实际调整）
COPY . /app

# 设置容器启动时执行的命令（这里示例为运行测试脚本，你需要根据实际情况改成自己的入口命令）
CMD ["python", "run_tests.py"]
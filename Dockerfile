# 使用基于Debian的基础镜像（Debian系统通用性较好且软件包管理方便，你也可以根据喜好选择其他合适基础镜像）
FROM debian:latest

# 更新软件源列表，确保能获取到最新的软件包信息
RUN apt-get update

# 安装运行谷歌浏览器和ChromeDriver所需的依赖包
RUN apt-get install -y wget gnupg2 ca-certificates fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgbm1 libgcc1 libglib2.0-0 libgtk-3-0 libnspr4 libnss3 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 lsb-release xdg-utils

# 安装unzip工具，用于后续解压ChromeDriver压缩包
RUN apt-get install -y unzip

# 下载谷歌浏览器安装包
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

# 安装谷歌浏览器，处理可能出现的依赖安装问题（如果dpkg安装时出现依赖缺失等报错，apt-get install -f会自动修复并完成安装）
RUN dpkg -i google-chrome-stable_current_amd64.deb || apt-get install -f -y

# 下载ChromeDriver压缩包到指定目录（这里选择下载到 /tmp 目录，可根据实际情况调整）
RUN wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip -P /tmp/

# 进入存放ChromeDriver压缩包的目录（这里是 /tmp 目录）
WORKDIR /tmp

# 解压ChromeDriver压缩包，添加解压命令可能需要的文件权限（确保能正常读取和解压文件）
RUN chmod +r chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip

# 将解压后的ChromeDriver可执行文件移动到系统的可执行文件目录（一般是 /usr/local/bin/ ，确保其在PATH环境变量中可被找到）
RUN mv chromedriver /usr/local/bin/
RUN chmod +x /usr/local/bin/chromedriver

# 设置工作目录（可选，根据你的实际使用情况调整）
WORKDIR /app

# 可以将你的自动化测试代码复制到容器内（假设你的代码在本地当前目录下名为test.py，以下是示例，按实际调整）
COPY . /app

# 设置容器启动时执行的命令（这里示例为运行测试脚本，你需要根据实际情况改成自己的入口命令）
CMD ["python", "run_tests.py"]
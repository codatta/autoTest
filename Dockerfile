# 使用Ubuntu基础镜像
FROM ubuntu:20.04

# 安装必要的依赖
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    gnupg2 \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 下载并安装谷歌浏览器
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get update && \
    apt-get install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb

# 安装ChromeDriver
RUN CHROMEDRIVER_VERSION=$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE) && \
    wget https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    mv chromedriver /usr/local/bin/ && \
    chmod +x /usr/local/bin/chromedriver && \
    rm chromedriver_linux64.zip

# 安装Python和依赖
RUN apt-get install -y python3 python3-pip && \
    pip3 install --no-cache-dir -r requirements.txt

# 设置工作目录
WORKDIR /app

# 复制当前目录内容到容器内
COPY . .

# 设置无头模式运行谷歌浏览器
CMD ["python3", "run_tests.py"]  # 替换为您的主脚本
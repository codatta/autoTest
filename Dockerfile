# 使用官方Python基础镜像
FROM python:3.13-slim

# 设置工作目录
WORKDIR /app

# 复制当前目录内容到容器内
COPY . .

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    gnupg2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 下载并安装谷歌浏览器
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get update && \
    apt-get install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb

# 安装Python依赖
RUN pip install --no-cache-dir -r requirements.txt

# 设置无头模式运行谷歌浏览器
CMD ["python", "run_tests.py"]  # 替换为您的主脚本
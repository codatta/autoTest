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
    && wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update && apt-get install -y google-chrome-stable \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 安装Python依赖
RUN pip install --no-cache-dir -r requirements.txt

# 设置无头模式运行谷歌浏览器
CMD ["python", "run_tests.py"]
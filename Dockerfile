# 使用基础镜像
FROM python:3.13-slim

# 设置工作目录
WORKDIR /app

# 更新软件源并安装项目构建和运行所需的所有依赖（包括Python、pip以及ChromeDriver相关依赖）
RUN apt-get update && \
    apt-get install -y libglib2.0-0 libnss3 libgconf-2-4 libfontconfig1 python3 python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 复制项目文件到容器内工作目录
COPY. /app

# 安装项目所需的Python依赖包
RUN pip3 install -r requirements.txt

# 设置默认的入口点命令（可以通过外部传入的环境变量来覆盖）
ENV ENTRYPOINT_COMMAND="python run_tests.py"
ENTRYPOINT ["sh", "-c", "$ENTRYPOINT_COMMAND"]
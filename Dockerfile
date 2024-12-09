# 使用基础镜像
FROM python:3.13-slim

# 设置工作目录，可选，根据你的实际情况调整路径
WORKDIR /app

# 安装依赖包，更新软件源列表并安装ChromeDriver所需依赖库
RUN apt-get update && \
    apt-get install -y libglib2.0-0 libnss3 libgconf-2-4 libfontconfig1 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 安装Python及相关工具（假设你的项目依赖Python，根据实际情况调整版本等）
RUN apt-get install -y python3 python3-pip

# 复制项目文件到容器内工作目录（假设当前目录下有项目代码，将其复制到容器的 /app 目录下）
COPY. /app

# 安装项目所需的Python依赖包（假设项目有 requirements.txt 文件列出依赖）
RUN pip3 install -r requirements.txt

# 设置入口点
ENTRYPOINT ["python", "run_tests.py"]

# 使用基础镜像
FROM python:3.13-slim

# 设置工作目录
WORKDIR /app

# 复制项目文件到容器中
COPY . .

# 安装依赖
RUN pip install -r requirements.txt

# 设置入口点
ENTRYPOINT ["python", "run_tests.py"]

> dockerfile for hdata_minder

#### 编译镜像
    docker build -t sanic_name .

#### 创建容器
    docker run -d --restart=always -p 6668:6668 sanic_name:latest

#### 
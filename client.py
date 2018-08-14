import socket
#导入模块
client=socket.socket()
#实例初始化
ip_port=("127.0.0.1",8888)
# 设置IP和端口
client.connect(ip_port)
#连接主机
data=client.recv(1024)
# 接收主机信息
print(data.decode())
# 打印数据


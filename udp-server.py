import socket
import random
# 导入模块
sk=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# 创建实例
ip_port=("127.0.0.1",8888)
# 定义IP和端口
sk.bind(ip_port)
# 绑定监听

while True:
	print("正在等待接收数据。。。")
	data=sk.recv(1024)
	# 缓冲区大小字节
	print(data.decode())
	if data.decode()=="exit":
		print("用户退出")
		break


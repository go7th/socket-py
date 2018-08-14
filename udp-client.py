import socket
#导入模块
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#实例初始化
ip_port=("127.0.0.1",8888)
# 设置IP和端口
while True:
	msg_input=input("请输入发送的信息\n")
	client.sendto(msg_input.encode(),ip_port)
	if msg_input=="exit":
		print("已退出")
		break
# client.close()
	# data=client.recv(1024)
	# 接收主机信息
	# print(data.decode())
	# 打印数据
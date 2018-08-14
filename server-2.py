import socket
import random
# 导入模块
sk=socket.socket()
# 创建实例
ip_port=("127.0.0.1",8888)
# 定义IP和端口
sk.bind(ip_port)
# 绑定监听
sk.listen(5)
# 最大连接数
while True:
	print("正在等待接收数据。。。")
	# 提示信息
	conn,address=sk.accept()
	# 接收数据
	msg="连接成功"
	# 定义信息
	conn.send(msg.encode())
	# 发送信息，python3.X以上都是byte类型，如果发送str需要编码encode()
	while True:
		data=conn.recv(1024)
		# 缓冲区大小字节
		print(data.decode())
		if data ==b"exit":
			print("用户退出")
			break
		conn.send(data)
		# conn.send(str(random.randint(1,1000)).encode())
		# 退出判断
	conn.close()	
	# 关闭连接
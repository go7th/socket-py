import socketserver

class MyServer(socketserver.BaseRequestHandler):
	"""docstring for MyServer"""
	def __init__(self, arg):
		super(MyServer, self).__init__()
		self.arg = arg
	def setup(self):
		pass
	def handle(self):
		conn=self.request
		# 定义连接变量
		msg="hello world"
		conn.send(msg.encode())
		while True:
			data=conn.recv(1024)
			print(data.decode())
			if data==b"exit":
				break
			conn.send(data)
			conn.close()
			pass
		pass
	def finish(self):
		pass


if __name__ == "__main__":
	server=socketserver.ThreadingTCPServer(("127.0.0.1",8888),MyServer)
	# 创建多线程实例
	server.serve_forever()
	#开启异步多线程，等待连接
	pass
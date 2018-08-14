import socket
# 导入模块
sk=socket.socket()
# 创建实例
ip_port=("127.0.0.1",8888)
# 定义IP和端口
sk.bind(ip_port)
# 绑定监听
sk.listen(5)
# 最大连接数
print("正在等待接收数据。。。")
# 提示信息
conn,address=sk.accept()
# 接收数据
msg="hello world"
# 定义信息
conn.send(msg.encode())
# 发送信息，python3.X以上都是byte类型，如果发送str需要编码encode()
conn.close()
# 关闭连接
import socket

print("程序开始")
#   创建套接字
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#   设置IP和端口
host = '192.168.2.171'
port = 60443
#   bind绑定该端口
mySocket.bind((host, port))
#   监听
mySocket.listen(10)

while True:
    #   接收客户端连接
    print("等待连接....")
    client, address = mySocket.accept()
    print("新连接")
    print("IP is %s" % address[0])
    print("port is %d\n" % address[1])
    client.sendall(bytes("hello world!", encoding="utf-8"))

    while True:
        #   发送消息
        # msg = input("----------------------发送:")
        # client.send(msg.encode())
        # print("发送完成")
        # if msg == "EOF":
        #     break
        # if msg == "quit":
        #     client.close()
        #     mySocket.close()
        #     print("程序结束\n")
        #     exit()
        #   读取消息
        msg = client.recv(1024)
        print("----------------------读取:", msg.decode())
        print("读取完成")
        if msg == b"EOF":
            break
        if msg == b"quit":
            client.close()
            mySocket.close()
            print("程序结束\n")
            exit()
        #     客户端断开连接
        if msg == b"":
            client.close()
            mySocket.close()
            print("程序结束\n")
            exit()

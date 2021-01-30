import socket


def client_handle(client,addr):
    while True:
        try:
            print(addr[1], "：", client.recv(1024).decode())
        except:
            client.close()
            print(addr[1], "离开了聊天室。")
            break


if __name__ == '__main__':
    target = "127.0.0.1"
    port = 6666
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((target,port))
    server.listen(10)
    print("服务器已开启，正在监听用户请求...")
    while True:
        # 与客户端连接
        client,addr = server.accept()
        print("连接地址： %s" % str(addr))
        sends = "欢迎来到聊天室。"
        client.send(sends.encode("utf-8"))
        client_handle(client,addr)
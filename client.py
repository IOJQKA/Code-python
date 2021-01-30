import socket


def send_info(client):
    sends = input("请输入发送的内容：")
    client.send(sends.encode("utf-8"))


if __name__ == '__main__':
    target = "127.0.0.1"
    port = 6666
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((target,port))
    msg = client.recv(1024)
    print(msg.decode("utf-8"))
    while True:
        send_info(client)
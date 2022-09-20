from socket import *

s_ip = 'localhost'
s_port = 12345
s_addr = (s_ip, s_port)

c_sock = socket(AF_INET, SOCK_STREAM)

c_sock.connect(s_addr)

while True:
    inputData = input("입력 문자열 :")
    c_sock.send(inputData.encode("utf-8"))

    print(c_sock.recv(1024).decode("utf-8"))
    if (inputData == 'q'):
        print("송신종료")
        break

c_sock.close()

# from socket import *

# s_ip = 'localhost'
# s_port = 9999
# s_addr = (s_ip, s_port)

# c_sock = socket(AF_INET, SOCK_STREAM)
# c_sock.connect(s_addr)

# data1 = 'Received data from client : '
# print(data1, c_sock.recv(1024).decode('utf-8'))
# data2 = 'Hello, TCP Server'
# c_sock.send(data2.encode("utf-8"))

# c_sock.close()

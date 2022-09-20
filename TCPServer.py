from socket import *

s_ip = 'localhost'
s_port = 12345
s_addr = (s_ip, s_port)

s_sock = socket(AF_INET, SOCK_STREAM)
s_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

s_sock.bind(s_addr)
s_sock.listen(2)

client, c_addr = s_sock.accept()
print(c_addr, "Now connected")

data = 'dummy'

while len(data):
    data = client.recv(1024).decode("utf-8")

    if data == 'q':
        print('\n수신 종료')
        break

print("수신 된 Data: ", data)
client.send(data.encode("utf-8"))

client.close()
s_sock.close()

#**********TCP서버**************#
# from socket import *

# s_ip = 'localhost'
# s_port = 9999
# s_addr = (s_ip, s_port)

# s_sock = socket(AF_INET, SOCK_STREAM)
# s_sock.bind(s_addr)
# s_sock.listen(2)

# client, c_addr = s_sock.accept()
# print(c_addr, 'is connected')

# data1 = 'Thank you for connecting'
# client.send(data1.encode("utf-8"))
# data2 = 'Received data from client : '
# print(data2, client.recv(1024).decode('utf-8'))

# client.close()
# socket.close()

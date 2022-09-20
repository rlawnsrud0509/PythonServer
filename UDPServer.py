from http import client
from socket import *

s_ip = 'localhost'
s_port = 12346
s_addr = (s_ip, s_port)

s_sock = socket(AF_INET, SOCK_DGRAM)

# ****** TCP는 STREAM, UDP는 DGRAM 기억합시다******

s_sock.bind(s_addr)

s_sock.settimeout(10)
# 서버가 10초간 클라이언트의 접속을 기다림
# 즉 10초이내에 응답이 없으면 서버꺼짐

data, c_addr = s_sock.recvfrom(1024)

print("수신된 클라이언트 위치 : ", c_addr)
print("수신된 데이터는 ", data.decode("utf-8"))

s_sock.close()

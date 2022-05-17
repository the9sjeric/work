import telnetlib
import re
import time
username = "admin"
password = "aims@0571"
hostIP = "192.168.108.16"

telnet_connect = telnetlib.Telnet()
try:
    telnet_connect.open(hostIP)
    print("telent连接完毕！")
except:
    print("连接失败，请检查原因。")

telnet_connect.read_until(b"Username:", timeout=2)
telnet_connect.write(username.encode() + b"\n")
print("输入账号完毕！")

telnet_connect.read_until(b"Password", timeout=2)
telnet_connect.write(password.encode() + b"\n")
print("输入密码完毕！")

telnet_connect.read_until(b">", timeout=2)
telnet_connect.write(b"dis cur" + b"\n")
print("输入命令完毕！")


output = telnet_connect.read_until(b"more", timeout=5)
a = 0
while b"More" in output:
    print("有发现more")
    telnet_connect.write(b" ")
    output = telnet_connect.read_until(b"more", timeout=5)
    print(output.decode("utf-8"))
    print("有more")
    a = a + 1
    print(a)
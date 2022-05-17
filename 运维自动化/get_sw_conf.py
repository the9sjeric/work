import telnetlib

username = "admin"
password = "aims@0571"
hostIP = "192.168.108.16"

client = telnetlib.Telnet(host=hostIP, port=23, timeout=10)
print("输入连接地址完毕！")
client.set_debuglevel(0)

client.read_until(b"Username:", timeout=10)
client.write(username.encode() + b"\n")
print("输入账号完毕！")
client.read_until(b"Password", timeout=10)
client.write(password.encode() + b"\n")
print("输入密码完毕！")

client.read_until(b"<1850-6>", timeout=10)
client.write(b"dis cur" + b"\n")
print("输入命令完毕！")

output = client.read_until(b"return", timeout=10)
print(output)
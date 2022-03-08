from aip import AipNlp

""" 你的 APPID AK SK """
APP_ID = "25693310"
API_KEY = "252pe1hu4LwDyR4re59f4gRH"
SECRET_KEY = "dp1g8ijVQq4bErALnNnZ7naM1OWIWxys"

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

# TODO 自定义一条评论，并存储在变量text中
text = "大家好，我叫文军。"

# TODO 调用sentimentClassify接口，并将结果存储在result里
result = client.sentimentClassify(text)

# TODO 输出结果
print(result)
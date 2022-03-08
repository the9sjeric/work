from aip import AipImageClassify

""" 你的 APPID AK SK """
APP_ID = "25727998"
API_KEY = "i752GbrdR2LIDqRdVyQLKiU9"
SECRET_KEY = "rv0S4zE8rNxLG5fZSccpLzYL1bkIaxKD"

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

print(client)
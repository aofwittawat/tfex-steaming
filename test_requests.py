import requests
import json

# url = 'http://127.0.0.1:5000/signals'
heroku_url = "https://tfex-steaming.herokuapp.com/signals"  # webhook
ข้อมูลตัวอย่าง = {
    "SYMBOL": "S50U22",
    "ACTION": "Long",
    "PRICE": "950.1",
    "AMOUNT": "1",
    "PASSWORD": "272427"
}


ข้อมูลตัวอย่าง = json.dumps(ข้อมูลตัวอย่าง)

x = requests.post(heroku_url, data=ข้อมูลตัวอย่าง)
# x = requests.post(heroku_url, data = ข้อมูลตัวอย่าง)

print(x.text)

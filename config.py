import os


# แก้ไขเวลา Deploy ขึ้น heroku ใช้ ENV variable เพื่อปกป้อง api key
# heroku config:set APP_ID=xxx
# heroku config:set API_SECRET=xxx


API_ID = os.getenv("API_ID")
API_SECRET = os.getenv("API_SECRET")


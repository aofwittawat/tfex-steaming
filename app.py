from flask import Flask, request
from settrade.openapi import Investor
from config import *

app = Flask(__name__)


@app.route("/")  # add path url
def hello_world():
    return "Cryto-5min Ready to use!"


@app.route("/webhook")
def webhook():
    return "This is url for webhook!"
# {
#     "SYMBOL": "S50U22",
#     "ACTION": "Long", // "Long Exit"
#     "PRICE" : "970",
#     "AMOUNT" : "20",
#     "PASSWORD":"272427"
# }


@app.route("/signals", methods=['POST'])
def signals():
    print("Someone Post Signals to me !")
    signal = request.data.decode("utf-8")
    import json
    signal = json.loads(signal)  # เปลี่ยนจาก json ให้เป็น dictionary
    
    symbol = str(signal["SYMBOL"])
    action = str(signal["ACTION"])
    price = float(signal["PRICE"])
    amount = float(signal["AMOUNT"])
    password = str(signal["PASSWORD"])

    if password != "272427":
        print("WRONG PASSWORD")
        return "403"
    
    print("ได้รับสัญญาณการซื้อขาย ดังนี้.....")
    print("symbol: " + str(symbol))
    print("action: " + str(action))
    print("price: " + str(price))
    print("amount: " + str(amount))
    print("บอทเริ่มทำคำสั่งซื้อขายอัตโนมัติ ไปที่ Steaming")
    
    # ======================== Execute ==============================
    
    investor = Investor(
                    app_id=API_ID,                                
                    app_secret=API_SECRET,
                    broker_id="003",                                           
                    app_code="ALGO",
                    is_auto_queue = False)

    deri = investor.Derivatives(account_no="01520870")
    if action == "Long":
        OPEN_LONG = deri.place_order(
            symbol=symbol,
            price=float(price),
            volume=int(amount),
            side="LONG",
            position="OPEN",
            pin="272427")
    elif action == "Long Exit":
        CLOSE_LONG = deri.place_order(
            symbol=symbol,
            price=float(price),
            volume=int(amount),
            side="LONG",
            position="CLOSE",
            pin="272427")
    elif action == "Short":
        OPEN_SHORT = deri.place_order(
            symbol=symbol,
            price=float(price),
            volume=int(amount),
            side="SHORT",
            position="OPEN",
            pin="272427")
    elif action == "Short Exit":
        CLOSE_SHORT = deri.place_order(
            symbol=symbol,
            price=float(price),
            volume=int(amount),
            side="SHORT",
            position="CLOSE",
            pin="272427")
        

    
    return "200"


if __name__ == "__main__":
    app.run()  # สั่งให้ app run !

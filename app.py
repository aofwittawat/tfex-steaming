from os import system
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
#     "ACTION": "Long", // "Long Exit" // "Short" // "Short Exit"
#     "PRICE" : "970",
#     "AMOUNT" : "20",
#     "PASSWORD":"272427",
#     "SYSTEM" :"xxxxx"
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
    system = str(signal["SYSTEM"])

    if password != "272427":
        print("WRONG PASSWORD")
        return "403"

    if action == "Long":
        price_c = round((price + 0.2), 1)
    elif action == "Short":
        price_c = round((price - 0.2), 1)
    elif action == "Long Exit":
        price_c = round((price - 0.5), 1)
    elif action == "Short Exit":
        price_c = round((price + 0.5), 1)

    print("ได้รับสัญญาณการซื้อขาย ดังนี้.....")
    print("symbol: " + str(symbol))
    print("action: " + str(action))
    print("price: " + str(price_c))
    print("amount: " + str(amount))
    print("บอทเริ่มทำคำสั่งซื้อขายอัตโนมัติ ไปที่ Steaming")

    # ดึงค่า SL ออกจาก order
# ======================================LINE NOTIFY==================================================
    message = f"👇👇👇👇 \n🤖ได้รับสัญญาณการซื้อขาย ดังนี้..... \n🤖รูปแบบการเทรด {action} {symbol} \n🤖ด้วยระบบ {system}\n ที่ราคา {price}"
    # Line notify Process
    from line_notify import LineNotify
    Access_Token = "MiUHQg2hMDPv81rSWcLPlMj9Fo47jqCxI71kaMdl0hU"  # generate line notify
    Access_Token_2 = "gR3C9xC50xpKIJ52baAdi0myhhUTv8RENEoCe6J4gmy"  # generate line notify
    notify = LineNotify(Access_Token)
    notify_2 = LineNotify(Access_Token_2)
    notify.send(message)  # ส่งไปที่ห้องแชท tfex_test ที่ tfex meeting
    notify_2.send(message)  # ส่งไปที่ห้องแชท robot trade indy

# =====================================FUTURE EXCECUTE================================================

    # ======================== Execute ==============================
    for member in members:
        try:
            investor = Investor(
                app_id=member[0],
                app_secret=member[1],
                broker_id="003",
                app_code="ALGO",
                is_auto_queue=False)
            deri = investor.Derivatives(account_no=member[2])
            if action == "Long":
                OPEN_LONG = deri.place_order(
                    symbol=symbol,
                    price=float(price_c),
                    volume=int(amount),
                    side="LONG",
                    position="OPEN",
                    pin=member[3])
            elif action == "Long Exit":
                CLOSE_LONG = deri.place_order(
                    symbol=symbol,
                    price=float(price_c),
                    volume=int(amount),
                    side="SHORT",
                    position="CLOSE",
                    pin=member[3])
            elif action == "Short":
                OPEN_SHORT = deri.place_order(
                    symbol=symbol,
                    price=float(price_c),
                    volume=int(amount),
                    side="SHORT",
                    position="OPEN",
                    pin=member[3])
            elif action == "Short Exit":
                CLOSE_SHORT = deri.place_order(
                    symbol=symbol,
                    price=float(price_c),
                    volume=int(amount),
                    side="LONG",
                    position="CLOSE",
                    pin=member[3])
        except Exception as e:
            print(e)

    return "200"


if __name__ == "__main__":
    app.run()  # สั่งให้ app run !

from settrade.openapi import Investor

investor = Investor(
                app_id="8xTYO94JJUANHbuD",                                
                app_secret="Dy4E345Ksb7qNRvLuuZizWGrSNursvKwQ3Hgro92YlA=",
                broker_id="003",                                           
                app_code="ALGO",
                is_auto_queue = False)

deri = investor.Derivatives(account_no="01520870")
OPEN_LONG = deri.place_order(
    symbol="S50U22",
    price=950,
    volume=1,
    side="LONG",
    position="OPEN",
    pin="272427")
CLOSE_LONG = deri.place_order(
    symbol="S50U22",
    price=950,
    volume=1,
    side="LONG",
    position="CLOSE",
    pin="272427")
OPEN_SHORT = deri.place_order(
    symbol="S50U22",
    price=950,
    volume=1,
    side="SHORT",
    position="OPEN",
    pin="272427")
CLOSE_SHORT = deri.place_order(
    symbol="S50U22",
    price=950,
    volume=1,
    side="SHORT",
    position="CLOSE",
    pin="272427")


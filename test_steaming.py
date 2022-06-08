import settrade.openapi

from settrade.openapi import Investor

#########################Login Part###########################
investor = Investor(
    app_id="8xTYO94JJUANHbuD",                                 # Your app ID
    app_secret="Dy4E345Ksb7qNRvLuuZizWGrSNursvKwQ3Hgro92YlA=",  # Your app Secret
    broker_id="003",
    app_code="ALGO",
    is_auto_queue=False)


# Your account number
deri = investor.Derivatives(account_no="01520870")
order_list = deri.get_orders()

account_no = order_list["data"][0]["side"]
print(account_no)

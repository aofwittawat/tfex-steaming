import settrade.openapi

from settrade.openapi import Investor

#########################Login Part###########################
investor = Investor(
                app_id="8xTYO94JJUANHbuD",                                 # Your app ID
                app_secret="Dy4E345Ksb7qNRvLuuZizWGrSNursvKwQ3Hgro92YlA=", # Your app Secret
                broker_id="003",                                           
                app_code="ALGO",
                is_auto_queue = False)


deri = investor.Derivatives(account_no="01520870")               # Your account number
account_info = deri.get_account_info()
print(account_info) 
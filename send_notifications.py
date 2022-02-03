# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
import json
from twilio.rest import Client
import datetime
from datetime import date
import time
# Find these values at https://twilio.com/user/account
# To set up environmental variables, see http://twil.io/secure
today = date.today()
dayOfWeek = today.strftime("%A")
print(dayOfWeek)
with open("config.json", "r") as f:
    configs = json.load(f)
    account_sid = configs["token"]
    auth_token = configs["sid"]
choreFP = open("chores.json")
chores = json.load(choreFP)
logName = time.strftime("log/NotificationBot_%Y_%m_%d_%H_%M.txt")
log = open(logName, "w")
#client = Client(account_sid, auth_token)


for person in chores[dayOfWeek]:
    print("Texting "+person["Name"]+" at "+person["Phone"])
# client.api.account.messages.create(
#     to="+12316851234",
#     from_="+15555555555",
#     body="Hello there!")

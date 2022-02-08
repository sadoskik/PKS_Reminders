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
with open("/home/ubuntu/PKS_Reminders/config.json", "r") as f:
    configs = json.load(f)
    account_sid = configs["sid"]
    auth_token = configs["token"]
choreFP = open("/home/ubuntu/PKS_Reminders/chores.json")
chores = json.load(choreFP)
logName = time.strftime("/home/ubuntu/PKS_Reminders/log/NotificationBot_%Y_%m_%d_%H_%M.txt")
log = open(logName, "w")
client = Client(account_sid, auth_token)

client.api.account.messages.create(
        to="+13015030799",
        from_="+14049742199",
        body="Messages being sent.")
for person in chores[dayOfWeek]:
    log.write("Texting "+person["Name"]+" at "+person["Phone"])
    log.write("\n")
    print(person["Name"])
    print(person["Phone"])
    client.api.account.messages.create(
        to=person["Phone"],
        from_="+14049742199",
        body="Reminder you have a chore today. Please remember to record it on the checkoff sheet.")

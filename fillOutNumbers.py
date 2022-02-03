import json
import re

f = open("chores.json", "r")
choresJson = json.load(f)

roster = open("roster.csv")
rosterText = roster.readlines()

for weekday in choresJson:
    for person in choresJson[weekday]:
        print(person)
        for row in rosterText:
            if(row.find(person["Name"]) > -1):
                number = re.search(
                    ",[\d-]{12}",
                    row
                ).group()
                break
        number = number.replace("-", "")
        number = number.replace(",", "")
        number = "+1" + number
        print(number)
        person["Phone"] = number

f = open("chores.json", "w")
json.dump(choresJson, f)
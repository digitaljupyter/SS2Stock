print("Step 1: randomize number")
import random
import os
import json
import datetime

fluctuation = json.load(open("Fluctuate.json", "r"))

fluctuation_amount = random.randrange(fluctuation["start"], fluctuation["end"])

old_amount = json.load(open("Currency.json", "r"))["networth"]

print("Fluctuating to: " + str(fluctuation_amount))

with open("Currency.json", "w") as f:
  # THIS IS WHAT WE WILL UPDATE
  f.write("""{
  "currency_name": "SimBuck",
  "networth": """ + str(fluctuation_amount) + """,
  "currency_short": "S$"
}
""".strip().strip())

print("Commiting to git")

os.system("git add Currency.json")

os.system("git commit -m \"[auto] update for " + datetime.datetime.now().strftime("%m/%d/%Y") + "\"")

## Add updates

from discord_webhook import DiscordWebhook

url = json.load(open("env.json"))["url"]
webhook = DiscordWebhook(url=url, content='Update to SimBuck value! Old: **' + str(old_amount) + "**\nNew: **" + str(fluctuation_amount) + "**\nValue went ***" +
  ("Down" if fluctuation_amount < old_amount else "Up") + "***!")
response = webhook.execute()

# os.system("git push")

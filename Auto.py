print("Step 1: randomize number")
import random
import os
import json
import datetime

fluctuation = json.load(open("Fluctuate.json", "r"))

fluctuation_amount = random.randrange(fluctuation["start"], fluctuation["end"])

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

# os.system("git push")

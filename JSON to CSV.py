import json, csv

f = open("data.json")
data = json.load(f)
f.close()

c = open("data.csv", "w", newline="")
w = csv.writer(c)

w.writerow(data[0].keys())

for i in data:
    w.writerow(i.values())

c.close()
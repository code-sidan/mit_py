import csv

f = open("data.csv")
r = csv.reader(f)

c = 0
for i in r:
    c += 1

print(c)
f.close()
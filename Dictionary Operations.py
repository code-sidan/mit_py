d = {"a": 1, "b": 2}

print(d["a"])

d["c"] = 3
d["a"] = 10

del d["b"]

d2 = {"d": 4}
d.update(d2)

print(d)
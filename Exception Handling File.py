try:
    f = open("abc.txt")
    print(f.read())
except FileNotFoundError:
    print("file not found")
except PermissionError:
    print("no permission")
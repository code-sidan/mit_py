f = open("file.txt", "w")
f.write("hello")
f.close()

f = open("file.txt", "r")
print(f.read())
f.close()

f = open("file.txt", "a")
f.write(" world")
f.close()
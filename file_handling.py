file = open("file.txt", "w")
file.write("there is nothing we can do\n")
file.close()

file = open("file.txt", "r")
print(file.read())
file.close()

file = open("file.txt", "a")
file.write("this is a virtual world....\n")
file.close()

file = open("file.txt", "r")
print("Updated file contents:")
print(file.read())
file.close()
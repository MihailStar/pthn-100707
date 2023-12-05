# 2
try:
    f = open("abc.txt")
    f.read(1)
    f.close()
except FileNotFoundError:
    print("File Not Found")

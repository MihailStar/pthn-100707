# 2
cities = input().split()
iterator = iter(cities)

for _ in range(2):
    print(next(iterator))


# 3
string = input()
iterator = iter(string)

for char in iterator:
    if char == " ":
        break
    print(char, end="")


# 4
digits = input()
iterator = iter(digits)

for _ in range(len(digits)):
    print(next(iterator), end=" ")

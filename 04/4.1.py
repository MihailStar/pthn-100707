# 1
n1, n2 = map(float, input().split())

if n1 > n2:
    print(n1)
else:
    print(n2)


# 2
s = input().lower()

if s == s[::-1]:
    print("ДА")
else:
    print("НЕТ")


# 3
m, n = map(int, input().split())
div, mod = divmod(m, n)

if mod == 0:
    print(div)
else:
    print(f"{m} на {n} нацело не делится")


# 4
a, b, c = map(int, input().split())

if c**2 == a**2 + b**2:
    print("ДА")
else:
    print("НЕТ")


# 5
d = input()

if d[-1] == "7":
    print("ДА")
else:
    print("НЕТ")


# 6
s = input()

if "t" in s and "h" in s and "o" in s:
    print("ДА")
else:
    print("НЕТ")


# 7
cities = input().split()

if "Москва" in cities:
    cities.remove("Москва")

print(*cities)


# 8
a, b, c, d = map(int, input().split())

if a >= c + 2 and b >= d + 2 or a >= d + 2 and b >= c + 2:
    print("ДА")
else:
    print("НЕТ")


# 9
d = input()

if sum(map(int, d[:3])) == sum(map(int, d[3:])):
    print("ДА")
else:
    print("НЕТ")


# 10
t = float(input())

if t % (2 + 3) <= 3:
    print("green")
else:
    print("red")

# 1
a = 7
b = -4
c = 3

print(a, b, c)


# 2
a = 7
b = -4
c = 3

print(a, b, c, sep="\n")


# 3
s1 = "Hello"
s2 = "Balakirev"

print(s1, end=" ")
print(s2)


# 4
s1, s2 = map(str.strip, input().split())

print("Word 1:", s1, "|", "Word 2:", s2)


# 5
n1, n2 = map(int, input().split())

print(n1**n2)


# 8
n1, n2 = map(float, input().split())

print(n1 + n2)


# 9
x, y = map(int, input().split())

print(x + y + x * 2 + y * 4)


# 10
h = float(input())
w = float(input())

print(h * 2 + w * 2)


# 11
from math import pi

print(round(pi, 3))


# 12
n = float(input())

print("Вы ввели число " + str(n))

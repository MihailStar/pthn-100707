# 5
from math import trunc

n = float(input())

print(trunc(n) % 3 == 0)
# print(int(n) % 3 == 0)


# 6
from math import modf

x = float(input())

print(modf(x)[0] > 0.5)


# 7
a, b = map(int, input().split())

print(a % b == 0)


# 10
a, b, c = map(int, input().split())

print((a + b) > c and (a + c) > b and (b + c) > a)


# 11
n = float(input())

print(0 <= n <= 2 or 10 <= n <= 20)

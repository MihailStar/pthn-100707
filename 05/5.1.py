# 2
from typing import List

n, m = map(int, input().split())
i = n
squares_of_ints: List[int] = []

while i <= m:
    squares_of_ints.append(i**2)
    i += 1

print(*squares_of_ints)


# 3
x = float(input())
counter = 2

while counter < 11:
    print(round(x * counter, 1), end=" ")
    counter += 1


# 4
n = int(input())
i = 1
result = 0.0

while i <= n:
    result += 1 / i
    i += 1

print(round(result, 3))


# 5
num = 1
total = 0

while num != 0:
    num = int(input())
    total += num

print(total)


# 6
string = input()
i = 1
result = string[0]

while i < len(string):
    if string[i] == "-" and result[-1] == "-":
        i += 1
        continue

    result += string[i]
    i += 1

print(result)


# 7
digits = input()
i = 0
result = 1

while i < len(digits):
    result *= int(digits[i])
    i += 1

print(result)


# 8
n = int(input())
a, b = 1, 1
i = 0

while i < n:
    print(a, end=" ")
    a, b = b, a + b
    i += 1


# 9
n = int(input())
a = 1
i = 3

while i < n:
    a *= 2
    i += 3

print(a)


# 10
n = int(input())
i = 0
account = 1000

while i < n:
    account += account * 0.05
    i += 1

print(round(account, 2))


# 11
n, m = map(int, input().split())
i = n + 1

while i < m:
    print(i, end=" ")
    i += 2


# 12
i = 2
n = 47 * i + 43

while n < 1000:
    n = 47 * i + 43
    if n % 3 == 0:
        print(n, end=" ")
    i += 1

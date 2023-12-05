# 2
*lst, x, y, z = input().split()

print(*lst)


# 3
print(tuple(input().split()))


# 4
a, b = (int(d) for d in input().split())

print(*range(a, b + 1))


# 5
print(*(*input().split(), *input().split()))


# 6
import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))
menu = {"Главная": "home", "Архив": "archive", "Новости": "news"}
menu = {**menu, **dict(pair.split("=") for pair in lst_in)}

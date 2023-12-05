# 1
m = """
1. Введение в Python
2. Строки и списки
3. Условные операторы
4. Циклы
5. Словари, кортежи и множества
6. Выход
"""
menu = m.strip().split("\n")
i = int(input()) - 1

if i == 0:
    print(menu[i])
elif i == 1:
    print(menu[i])
elif i == 2:
    print(menu[i])
elif i == 3:
    print(menu[i])
elif i == 4:
    print(menu[i])
elif i == 5:
    print(menu[i])


# 2
n1, n2, n3 = map(int, input().split())

if n2 >= n1 <= n3:
    print(n1)
elif n1 >= n2 <= n3:
    print(n2)
elif n1 >= n3 <= n2:
    print(n3)


# 3
weight = float(input())

if weight <= 60:
    print(1)
elif weight <= 64:
    print(2)
elif weight <= 69:
    print(3)
else:
    print(4)


# 4
index_digit = input()

if index_digit == "1":
    print("понедельник")
elif index_digit == "2":
    print("вторник")
elif index_digit == "3":
    print("среда")
elif index_digit == "4":
    print("четверг")
elif index_digit == "5":
    print("пятница")
elif index_digit == "6":
    print("суббота")
elif index_digit == "7":
    print("воскресенье")


# 5
index_digit = input()

if index_digit in ["1", "3", "5", "7", "8", "10", "12"]:
    print("31")
elif index_digit in ["4", "6", "9", "11"]:
    print("30")
elif index_digit in ["2"]:
    print("28")


# 6
DAYS_IN_MONTHS = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

m, d = map(int, input().split())
prev_m = m
prev_d = d - 1
next_m = m
next_d = d + 1

if d == 1:
    prev_m = m - 1
    prev_d = DAYS_IN_MONTHS[m - 1 - 1]
elif d == DAYS_IN_MONTHS[m - 1]:
    next_m = m + 1
    next_d = 1


print(
    "{mm}.{dd}".format(mm=f"{prev_m}".rjust(2, "0"), dd=f"{prev_d}".rjust(2, "0")),
    "{mm}.{dd}".format(mm=f"{next_m}".rjust(2, "0"), dd=f"{next_d}".rjust(2, "0")),
)


# 7
DAY_OF_WEEK = (
    "понедельник",
    "вторник",
    "среда",
    "четверг",
    "пятница",
    "суббота",
    "воскресенье",
)

k = int(input())

print(DAY_OF_WEEK[k % len(DAY_OF_WEEK) - 1])

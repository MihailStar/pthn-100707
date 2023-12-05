# 2
p = [0] * 10
counter = 0

while counter < 5:
    i = int(input())
    if p[i] == 1:
        continue
    p[i] = 1
    counter += 1

print(*p)


# 3
product_of_numbers = 1

while True:
    number = int(input())
    if number < 0:
        continue
    if number == 0:
        break
    product_of_numbers *= number

print(product_of_numbers)


# 4
cities = input().split()
i = 0

while i < len(cities):
    if len(cities[i]) < 6:
        print("НЕТ")
        break
    i += 1
else:
    print("ДА")


# 5
students = input().split()
i = 0

while i < len(students):
    student = students[i]
    if student[0].lower() == student[-1].lower():
        print("ДА")
        break
    i += 1
else:
    print("НЕТ")


# 6
from typing import List

n = int(input())
i = 3
result: List[int] = []

if n > 99:
    print("слишком большое значение n")
else:
    while i <= n:
        if i % 3 == 0 and i % 5 == 0:
            result.append(i)
        i += 3
    else:
        print(*result)


# 7
n = int(input())
i = 1

while i**2 <= n:
    i += 1

print(i)


# 8
x = int(input())
day = 1
distance = 10

while distance < x:
    distance += distance * 0.1
    day += 1

print(day)


# 9
import sys

book_names = list(map(str.strip, sys.stdin.readlines()))
i = 0

while i < len(book_names):
    book_name = book_names[i]
    if len(book_name.split()) == 1:
        print(book_name, end=" ")
    i += 1

# 1
from typing import List

string = input()
indexs: List[int] = []

for i in range(len(string) - 1):
    if string[i] == "р" and string[i + 1] == "а":
        indexs.append(i)

print(*indexs if indexs else [-1])


# 2
inputed_phone_number = input()
template_d = "1234567890"
template = "+7(ddd)ddd-dd-dd"

for i, _char in enumerate(inputed_phone_number):
    if (template[i] == inputed_phone_number[i]) or (
        template[i] == "d" and inputed_phone_number[i] in template_d
    ):
        continue

    print("НЕТ")
    break
else:
    print("ДА")


# 3
inputed_expression = input()
operands = []
operators = []
temp = ""

for char in inputed_expression:
    if char == " ":
        continue
    if char == "-" or char == "+":
        operators.append(char)
        operands.append(temp)
        temp = ""
    else:
        temp += char
else:
    operands.append(temp)
    temp = ""

result = int(operands[0])

for i in range(len(operators)):
    if operators[i] == "-":
        result -= int(operands[i + 1])
    else:
        result += int(operands[i + 1])

print(result)


# 4
inputed_digs = input().split()

for i, _dig in enumerate(inputed_digs):
    print(int(inputed_digs[i]) ** 2, end=" ")


# 5
inputed_digs = input().split()

for dig in inputed_digs:
    print(dig, dig, end=" ")


# 6
from math import inf

digits = input().split()
min = inf

for i in range(len(digits)):
    num = float(digits[i])
    if num < min:
        min = num

print(min)


# 7
digits = input().split()

for i, _ in enumerate(digits):
    num = float(digits[i])
    print(-1.0 if num < 0 else num, end=" ")

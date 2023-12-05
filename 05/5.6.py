# 1
from typing import List

n = int(input())
matrix: List[List[int]] = []

for y in range(n):
    row: List[int] = []
    for x in range(n):
        row.append(1)
    matrix.append(row)

for y in matrix:
    y[-1] = 5

for y in matrix:
    print(*y)


# 2
import re as regexp
import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))

for row in lst_in:
    print(regexp.sub(r" +", "-", row))


# 3
n = int(input())

for i in range(2, n):
    for d in range(2, i - 1):
        if i % d == 0:
            break
    else:
        print(i, end=" ")


# 4
import sys
from typing import List

s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]


def have_distance(mtrx: List[List[int]]) -> bool:
    """@tutorial https://stepik.org/lesson/567042/step/5?discussion=5028109&unit=561316"""
    for y in range(len(mtrx) - 1):
        for x in range(len(mtrx[0]) - 1):
            if mtrx[y][x] + mtrx[y][x + 1] + mtrx[y + 1][x + 1] + mtrx[y + 1][x] > 1:
                return False
    return True


print("ДА" if have_distance(lst_in) else "НЕТ")


# 5
import sys
from typing import List

s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]


def is_symmetrical_about_main_diagonal(mtrx: List[List[int]]) -> bool:
    """@tutorial https://stepik.org/lesson/567042/step/6?discussion=4835813&unit=561316"""
    for y, row in enumerate(mtrx):
        for x in range(len(row)):
            if mtrx[y][x] != mtrx[x][y]:
                return False
    return True


print("ДА" if is_symmetrical_about_main_diagonal(lst_in) else "НЕТ")


# 6
from typing import List

nums: List[int] = [int(dig) for dig in input().split()]

for i in range(len(nums)):
    min_i = i

    for j in range(i + 1, len(nums)):
        if nums[j] < nums[min_i]:
            min_i = j

    nums[i], nums[min_i] = nums[min_i], nums[i]

print(*nums)


# 7
from typing import List

nums: List[int] = [int(dig) for dig in input().split()]

for i in range(len(nums) - 1):
    for j in range(len(nums) - 1 - i):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print(*nums)


# 8
n = int(input())
coins = [64, 32, 16, 8, 4, 2, 1]
i = 0

while i < len(coins):
    coin = coins[i]
    number_of_coins, rest = divmod(n, coin)
    n = rest

    if number_of_coins > 0:
        for _ in range(number_of_coins):
            print(coin, end=" ")

    i += 1

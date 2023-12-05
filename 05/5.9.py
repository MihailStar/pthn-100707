# 1
import sys

s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

print(
    *[
        lst_in[y][x]
        for y in range(len(lst_in) - 1, -1, -1)
        for x in range(len(lst_in[y]) - 1, -1, -1)
    ]
)


# 2
from math import sqrt

digs = input().split()
nums = [int(dig) for dig in digs]
size = int(sqrt(len(digs)))
lst = [nums[start : start + size] for start in range(0, len(digs), size)]

print(lst)


# 3
t = [
    "– Скажи-ка, дядя, ведь не даром",
    "Я Python выучил с каналом",
    "Балакирев что раздавал?",
    "Ведь были ж заданья боевые,",
    "Да, говорят, еще какие!",
    "Недаром помнит вся Россия",
    "Как мы рубили их тогда!",
]
lst = [[word for word in line.split() if len(word) > 3] for line in t]

print(lst)


# 4
import sys

s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

for row in [[row[x] for row in lst_in] for x in range(len(lst_in[0]))]:
    print(*row)

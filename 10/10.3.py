# 2
import random

a, b = map(int, input().split())

random.seed(1)
print(round(random.uniform(a, b), 2))


# 3
import random

a, b = map(int, input().split())

random.seed(1)
print(random.randint(a, b))


# 4
import random

cities = input().split()

random.seed(1)
print(random.choice(cities))


# 5
import random
import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))

for line in lst_in:
    row = line.split()

    random.seed(1)
    random.shuffle(row)

    print(*row)


# 6
import random

students = input().split()

random.seed(1)
print(*random.sample(students, 3))


# 7
import random
from typing import List

N = int(input())
M = 10
P = [[0] * N for _ in range(N)]


def check(_field: List[List[int]], _y: int, _x: int) -> bool:
    for y in (_y - 1, _y, _y + 1):
        if y < 0 or y > N - 1:
            continue
        for x in (_x - 1, _x, _x + 1):
            if x < 0 or x > N - 1:
                continue

            if _field[y][x] != 0:
                return False

    return True


i = M

while i > 0:
    y = random.randint(0, N - 1)
    x = random.randint(0, N - 1)

    if check(P, y, x):
        P[y][x] = 1
        i -= 1

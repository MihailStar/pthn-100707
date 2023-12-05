# 3
from typing import Tuple

inputed = tuple(int(dig) for dig in input().split())
t: Tuple[float, ...] = (3.4, -56.7)
t = t + inputed

print(t)


# 4
cities = tuple(input().split())

if "Москва" not in cities:
    cities += ("Москва",)

print(*cities)


# 5
cities = tuple(input().split())

try:
    index_ulyanovsk = cities.index("Ульяновск")
    print(*cities[:index_ulyanovsk] + cities[index_ulyanovsk + 1 :])
except ValueError:
    print(*cities)


# 6
students = tuple(input().lower().split())

print(*(student for student in students if "ва" in student))


# 7
from typing import Dict

nums = tuple(int(dig) for dig in input().split())
temp: Dict[int, None] = dict.fromkeys(nums)

print(*tuple(temp))


# 8
from collections import defaultdict
from typing import DefaultDict

nums = tuple(int(dig) for dig in input().split())
num_to_count: DefaultDict[int, int] = defaultdict(lambda: 0)

for num in nums:
    num_to_count[num] += 1

for i, num in enumerate(nums):
    if num_to_count[num] > 1:
        print(i, end=" ")


# 9
n = int(input())
t = (
    (1, 0, 0, 0, 0),
    (0, 1, 0, 0, 0),
    (0, 0, 1, 0, 0),
    (0, 0, 0, 1, 0),
    (0, 0, 0, 0, 1),
)

for y in range(n):
    print(*t[y][:n])


# 10
import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))

print(tuple(tuple(pair.split()) for pair in lst_in))

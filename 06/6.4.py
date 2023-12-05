# 3
s = set(float(num) for num in input().split())

print(*sorted(s))


# 4
print(len(set(input().lower().split())))


# 5
from typing import Set

inputed = input()
non_repeating_digs: Set[int] = set()

for char in inputed:
    if char.isdigit():
        non_repeating_digs.add(int(char))

if len(non_repeating_digs) > 0:
    print(*sorted(non_repeating_digs))
else:
    print("НЕТ")


# 6
import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))

print(len(set(lst_in)))


# 7
import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))

print(len(set(line.split(": ")[0] for line in lst_in)))


# 8
from typing import Set

unique_cities: Set[str] = set()
city = input()

while city != "q":
    unique_cities.add(city)
    city = input()

print(len(unique_cities))

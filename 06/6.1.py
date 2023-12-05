# 3
from typing import Dict, List, Tuple

inputed = input().split()
pairs: List[Tuple[str, int]] = []

for pair in inputed:
    key, val = pair.split("=")
    pairs.append((key, int(val)))

d: Dict[str, int] = dict(pairs)

print(*sorted(d.items()))


# 4
import sys
from typing import Dict

lst_in = list(map(str.strip, sys.stdin.readlines()))
d: Dict[int, str] = {}

for line in lst_in:
    key, val = line.split("=")
    d[int(key)] = val

print(*sorted(d.items()))


# 5
d = {key: val for key, val in map(lambda pair: pair.split("="), input().split())}

print("ДА" if all((key in d for key in ["house", "True", "5"])) else "НЕТ")


# 6
d = dict((pair.split("=") for pair in input().split()))

for key in ["False", "3"]:
    if key in d:
        del d[key]

print(*sorted(d.items()))


# 7
from typing import Dict, List

phone_numbers = input().split()
d: Dict[str, List[str]] = {}

for phone_number in phone_numbers:
    plus, code, *rest = phone_number
    key = f"{plus}{code}"
    d[key] = d[key] + [phone_number] if key in d else [phone_number]

print(*sorted(d.items()))


# 8
import sys
from typing import Dict, List

lst_in = list(map(str.strip, sys.stdin.readlines()))
d: Dict[str, List[str]] = {}

for record in lst_in:
    val, key = record.split()
    d[key] = d.get(key, []) + [val]

print(*sorted(d.items()))


# 9
from math import sqrt
from typing import Dict

inputed = input()
cache: Dict[str, float] = {}

while inputed != "0":
    if inputed in cache:
        print(f"значение из кэша: {cache[inputed]}")
    else:
        cache[inputed] = round(sqrt(int(inputed)), 2)
        print(cache[inputed])

    inputed = input()


# 10
import sys
from typing import Dict

lst_in = list(map(str.strip, sys.stdin.readlines()))
cache: Dict[str, str] = {}

for url in lst_in:
    if url in cache:
        print(f"Взято из кэша: HTML-страница для адреса {url}")
        continue

    print(f"HTML-страница для адреса {url}")
    cache[url] = url

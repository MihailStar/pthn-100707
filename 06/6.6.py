# 2
first, *grades = input().split()
first = int(first)
d = {first + i: grade for i, grade in enumerate(grades)}

print(d[4])


# 3
import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))

print(len(set(lst_in)))


# 4
inputed = input().lower().split()

print(len({word for word in inputed if len(word) > 2}))


# 5
inputed = input().lower().split()
word_to_count = {key: inputed.count(key) for key in set(inputed)}
word_to_count.setdefault("и", 0)

print(word_to_count["и"])


# 6
import sys
from collections import defaultdict
from typing import Dict, Set

lst_in = list(map(str.strip, sys.stdin.readlines()))
d: Dict[str, Set[str]] = defaultdict(lambda: set())

for line in lst_in:
    author, title = line.split(": ")
    d[author].add(title)

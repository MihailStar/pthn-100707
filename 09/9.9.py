# 1
nums = map(int, input().split())

print(all(map(lambda num: num % 2 == 0, nums)))


# 2
nums = map(float, input().split())

print(any(map(lambda num: num < 0, nums)))


# 3
from typing import Any, Iterable


def is_string(items: Iterable[Any]) -> bool:
    return all(type(item) is str for item in items)


# 4
grades = map(int, input().split())

print("отчислен" if any(grade < 3 for grade in grades) else "учится")


# 5
from typing import List


def is_free(field: List[List[str]]) -> bool:
    return any(any(cell == "#" for cell in row) for row in field)

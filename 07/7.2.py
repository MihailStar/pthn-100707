# 1
def square(num: float) -> float:
    return num**2


print(square(float(input())))


# 2
def is_triangle(a: int, b: int, c: int) -> bool:
    return a + b > c and b + c > a and c + a > b


# 3
def is_large(string: str) -> bool:
    return len(string) > 2


# 4
def is_even(number: int) -> bool:
    return number % 2 == 0


for dig in iter(input, "1"):
    if is_even(int(dig)):
        print(dig)


# 5
def is_not_even(number: int) -> bool:
    return number % 2 == 1


nums = (int(dig) for dig in input().split())
lst = [num for num in nums if is_not_even(num)]

print(*lst)


# 6
tp = input().strip()

if tp == "RECT":

    def get_sq(a: int, b: int) -> int:
        return a * b

else:

    def get_sq(a: int) -> int:
        return a * a


# 7
def check_length(string: str) -> bool:
    return len(string) > 5


cities = input().split()
lst = [city for city in cities if check_length(city)]

print(*lst)


# 8
from typing import Tuple


def func(string: str) -> Tuple[str, int]:
    return (string, len(string))


d = {city: func(city)[1] for city in input().split()}

print(*sorted(d, key=lambda x: d[x]))


# 9
def foo(max: int, min: int) -> int:
    return max * min


inputed = input().split()

print(
    foo(
        max(int(dig) for dig in inputed),
        min(int(dig) for dig in inputed),
    )
)

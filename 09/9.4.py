# 1
cities = input().split()
filtered_cities = filter(lambda c: len(c) > 5, cities)

print(*(next(filtered_cities) for _ in range(3)))


# 2
import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))

print(
    *map(
        lambda item: item[0],
        filter(
            lambda item: int(item[1]) > 500,
            tuple(map(lambda pair: tuple(pair.split("=")), lst_in)),
        ),
    )
)


# 3
nums = map(int, input().split())

print(*filter(lambda num: len(str(abs(num))) == 2, nums))


# 4
print(
    *sorted(
        filter(
            lambda d: d % 2 == 0, map(int, set(input().split()) & set(input().split()))
        )
    )
)


# 5
import re as regexp

pattern = regexp.compile(r"^\w+@\w+\.\w+$")

print(*(email for email in input().split() if pattern.match(email)))

# 3
from typing import List


def get_even(*digs: str) -> List[str]:
    return [num for num in digs if int(num) % 2 == 0]


# 4
def get_biggest_city(*cities: str) -> str:
    biggest_city: str = cities[0]

    for i in range(1, len(cities)):
        if len(cities[i]) > len(biggest_city):
            biggest_city = cities[i]

    return biggest_city


# 5
from typing import Any, Tuple, Union


def get_data_fig(*sides: int, **kwargs: Union[bool, int]) -> Tuple[Any, ...]:
    perimeter = sum(sides)

    return (
        perimeter,
        *(kwargs[key] for key in ["type", "color", "closed", "width"] if key in kwargs),
    )


# 6
from typing import List


def verify(mtrx: List[List[int]]) -> bool:
    """@tutorial https://github.com/mihailstar/pthn-st/tree/master/05/5.6.py # 4"""
    for y in range(len(mtrx) - 1):
        for x in range(len(mtrx[0]) - 1):
            if mtrx[y][x] + mtrx[y][x + 1] + mtrx[y + 1][x + 1] + mtrx[y + 1][x] > 1:
                return False
    return True


def is_isolate() -> bool:
    pass


# 7
def str_min(*strs: str) -> str:
    return min(strs)


def str_min3(str_a: str, str_b: str, str_c: str) -> str:
    return str_min(str_a, str_b, str_c)


def str_min4(str_a: str, str_b: str, str_c: str, str_d: str) -> str:
    return str_min(str_a, str_b, str_c, str_d)

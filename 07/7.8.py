# 2
from typing import Callable

get_sq: Callable[[int], int] = lambda n: n**2


# 3
from typing import Callable, Optional

get_div: Callable[[int, int], Optional[float]] = (
    lambda num, divisor: None if divisor == 0 else num / divisor
)


# 4
print((lambda n: abs(n))(float(input())))


# 5
print((lambda s: "ra" in s)(input()))


# 6
from typing import Callable, Iterable, Optional, Tuple, TypeVar

T = TypeVar("T")


def filter_lst(
    it: Iterable[T], key: Optional[Callable[[T], bool]] = None
) -> Tuple[T, ...]:
    if key is None:
        return tuple(it)

    res = ()

    for x in it:
        if key(x):
            res += (x,)

    return res


nums = [int(num) for num in input().split()]

print(*filter_lst(nums, lambda num: True))
print(*filter_lst(nums, lambda num: num < 0))
print(*filter_lst(nums, lambda num: num > -1))
print(*filter_lst(nums, lambda num: num > 2 and num < 6))

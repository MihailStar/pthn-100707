# 1
from typing import Callable


def counter_add() -> Callable[[int], int]:
    return lambda arg: arg + 5


print((counter_add())(int(input())))


# 2
from typing import Callable


def counter_add(n: int) -> Callable[[int], int]:
    return lambda arg: arg + n


print((counter_add(2))(int(input())))


# 3
from typing import Callable


def wrap(tag: str = "h1") -> Callable[[str], str]:
    return lambda content: f"<{tag}>{content}</{tag}>"


print(wrap()(input()))


# 4
from typing import Callable


def wrap(tag: str = "div") -> Callable[[str], str]:
    return lambda content: f"<{tag}>{content}</{tag}>"


print(wrap(input())(input()))


# 5
from typing import Callable, List, Tuple, Union


def external(tp: str = "list") -> Callable[[str], Union[List[int], Tuple[int, ...]]]:
    def internal(digs: str) -> Union[List[int], Tuple[int, ...]]:
        nums = (int(dig) for dig in digs.split())

        return list(nums) if tp == "list" else tuple(nums)

    return internal


print(external(input())(input()))

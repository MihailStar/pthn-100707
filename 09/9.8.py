# 2
from typing import Union, overload


@overload
def get_add(a: int, b: int) -> int:
    ...


@overload
def get_add(a: int, b: float) -> float:
    ...


@overload
def get_add(a: float, b: int) -> float:
    ...


@overload
def get_add(a: float, b: float) -> float:
    ...


@overload
def get_add(a: str, b: str) -> str:
    ...


def get_add(
    a: Union[int, float, str], b: Union[int, float, str]
) -> Union[int, float, str, None]:
    if type(a) is bool or type(b) is bool:
        # because `print(isinstance(True, int))  # -> True`
        return None

    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b

    if isinstance(a, str) and isinstance(b, str):
        return a + b

    return None


# 3
from typing import Any, Iterable


def get_sum(iterable: Iterable[Any]) -> int:
    return sum(filter(lambda item: type(item) is int, iterable))


# 4
from typing import Any, Iterable


def get_even_sum(iterable: Iterable[Any]) -> int:
    return sum(filter(lambda item: type(item) is int and item % 2 == 0, iterable))


# 5
from typing import Any, List, Tuple, Union


def get_list_dig(iterable: Union[List[Any], Tuple[Any]]) -> List[Union[int, float]]:
    return [item for item in iterable if type(item) in (int, float)]

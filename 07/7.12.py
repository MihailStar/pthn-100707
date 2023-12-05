# 1
from functools import reduce
from typing import Callable


def set_start(start: int) -> Callable[[Callable[[str], int]], Callable[[str], int]]:
    def decorator(func: Callable[[str], int]) -> Callable[[str], int]:
        def wrapper(string_of_digs: str) -> int:
            return start + func(string_of_digs)

        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__

        return wrapper

    return decorator


@set_start(start=5)
def get_sum(string_of_digs: str) -> int:
    return reduce(
        lambda acc, num: acc + num, (int(dig) for dig in string_of_digs.split()), 0
    )


print(get_sum(input()))


# 2
from functools import wraps
from typing import Callable


def wrap(tag: str = "h1") -> Callable[[Callable[[str], str]], Callable[[str], str]]:
    def decorator(function: Callable[[str], str]) -> Callable[[str], str]:
        @wraps(function)
        def wrapper(string: str) -> str:
            return f"<{tag}>{function(string)}</{tag}>"

        return wrapper

    return decorator


@wrap("div")
def to_lower_case(string: str) -> str:
    return string.lower()


print(to_lower_case(input()))


# 3
import re as regexp
from functools import wraps
from typing import Callable

t = {
    **{"ё": "yo", "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e"},
    **{"ж": "zh", "з": "z", "и": "i", "й": "y", "к": "k", "л": "l", "м": "m"},
    **{"н": "n", "о": "o", "п": "p", "р": "r", "с": "s", "т": "t", "у": "u"},
    **{"ф": "f", "х": "h", "ц": "c", "ч": "ch", "ш": "sh", "щ": "shch", "ъ": ""},
    **{"ы": "y", "ь": "", "э": "e", "ю": "yu", "я": "ya"},
}


def replace(chars: str = " !?") -> Callable[[Callable[..., str]], Callable[..., str]]:
    pattern = regexp.compile(f"[{regexp.escape(chars + '-')}]+")

    def decorator(function: Callable[..., str]) -> Callable[..., str]:
        @wraps(function)
        def wrapper(*args: str) -> str:
            return pattern.sub("-", function(*args))

        return wrapper

    return decorator


@replace("?!:;,. ")
def cyr_to_lat(s: str) -> str:
    return "".join(t.get(char, char) for char in s.lower())


print(cyr_to_lat(input()))


# 4
from functools import wraps
from typing import Callable, Iterable, List


def get_sum(func: Callable[..., Iterable[int]]) -> Callable[..., int]:
    @wraps(func)
    def wrapper(*args: ...) -> int:
        return sum(func(*args))

    return wrapper


@get_sum
def get_list(digs: str) -> List[int]:
    """Функция для формирования списка целых значений"""
    return [int(dig) for dig in digs.split()]

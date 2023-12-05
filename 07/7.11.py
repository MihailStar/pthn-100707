# 1
from typing import Any, Callable, TypeVar


def get_sq(width: int, height: int) -> int:
    return width * height


R = TypeVar("R")


def func_show(func: Callable[..., R]) -> Callable[..., R]:
    def wrapper(*args: Any, **kwargs: Any) -> R:
        result = func(*args, **kwargs)
        print(f"Площадь прямоугольника: {result}")
        return result

    return wrapper


# 2
from typing import Any, Callable, List


def show_menu(func: Callable[[str], List[str]]) -> Callable[[str], List[str]]:
    def wrapper(*args: Any, **kwargs: Any) -> List[str]:
        menu = func(*args, **kwargs)

        for index, menu_item in enumerate(menu):
            print(f"{index + 1}. {menu_item}")

        return menu

    return wrapper


@show_menu
def get_menu(s: str) -> List[str]:
    return s.split()


# 3
from typing import Any, Callable, List


def decorator(func: Callable[[str], List[int]]) -> Callable[[str], List[int]]:
    def wrapper(*args: Any, **kwargs: Any) -> List[int]:
        return sorted(func(*args, **kwargs))

    return wrapper


@decorator
def get_list(s: str) -> List[int]:
    return [int(dig) for dig in s.split()]


print(*get_list(input()))


# 4
print(*sorted(dict(zip(input().split(), input().split())).items()))


# 5
import re as regexp
from typing import Any, Callable

t = {
    **{"ё": "yo", "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e"},
    **{"ж": "zh", "з": "z", "и": "i", "й": "y", "к": "k", "л": "l", "м": "m"},
    **{"н": "n", "о": "o", "п": "p", "р": "r", "с": "s", "т": "t", "у": "u"},
    **{"ф": "f", "х": "h", "ц": "c", "ч": "ch", "ш": "sh", "щ": "shch", "ъ": ""},
    **{"ы": "y", "ь": "", "э": "e", "ю": "yu", "я": "ya"},
}


def decorator(func: Callable[[str], str]) -> Callable[[str], str]:
    def wrapper(*args: Any, **kwargs: Any) -> str:
        return regexp.sub(r"-{2,}", "-", func(*args, **kwargs))

    return wrapper


@decorator
def cyr_to_lat(s: str) -> str:
    return "".join("-" if char in ": ;.,_" else t.get(char, char) for char in s.lower())


print(cyr_to_lat(input()))

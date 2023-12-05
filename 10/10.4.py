# 5
cmd = input()

match cmd:
    case "top" | "Top" | "TOP" | "right" | "Right" | "RIGHT" | "bottom" | "Bottom" | "BOTTOM" | "left" | "Left" | "LEFT":
        print(f"Команда {cmd.lower()}")
    case _:
        print("Неверная команда")


# 6
from typing import Any


def get_data(value: Any) -> int | float | str | None:
    match value:
        case bool():
            return None
        case int() | float() | str():
            return value
        case _:
            return None


# 7
from typing import Any


def get_data(value: Any) -> int | float | str | None:
    match value:
        case bool():
            return None
        case int() as i if i > 0:
            return value
        case float() as f if -100 <= f <= 100:
            return value
        case str():
            return value
        case _:
            return None

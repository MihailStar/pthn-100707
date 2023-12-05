# 4
from typing import Any, Dict, Tuple


def parse_json(data: Dict[str, Any]) -> Tuple[Any, Any] | None:
    match data:
        case {"access": bool() as a, "data": list() as d} if type(d[0]) == str:
            return (a, d[0])
        case {"id": ids, "data": [_, {"login": login}, _, _]}:
            return (ids, login)
        case _:
            return None


json_data = {
    "id": 2,
    "access": False,
    "data": ["26.05.2023", {"login": "1234", "email": "xxx@mail.com"}, 2000, 56.4],
}


# 5
from typing import Any, Dict, Tuple


def parse_json(data: Dict[str, Any]) -> Tuple[Any, Any] | None:
    match data:
        case {
            "access": True,
            "data": [_, {"login": str() as login, "email": str() as email}, *_],
        }:
            return (login, email)
        case {"id": ids, "data": [_, {"login": login}, _, _]}:
            return (ids, login)
        case _:
            return None


json_data = {
    "id": 2,
    "access": True,
    "data": ["26.05.2023", {"login": "1234", "email": "xxx@mail.com"}, 2000, 56.4],
}

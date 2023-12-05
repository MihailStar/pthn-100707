# 2
def get_rect_value(a: int, b: int, type: int = 0) -> int:
    return a * 2 + b * 2 if type == 0 else a * b


# 3
def check_password(password: str, chars: str = "$%!?@#") -> bool:
    if len(password) < 8:
        return False

    for char in chars:
        if char in password:
            return True

    return False


# 4
t = {
    **{"ё": "yo", "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e"},
    **{"ж": "zh", "з": "z", "и": "i", "й": "y", "к": "k", "л": "l", "м": "m"},
    **{"н": "n", "о": "o", "п": "p", "р": "r", "с": "s", "т": "t", "у": "u"},
    **{"ф": "f", "х": "h", "ц": "c", "ч": "ch", "ш": "sh", "щ": "shch", "ъ": ""},
    **{"ы": "y", "ь": "", "э": "e", "ю": "yu", "я": "ya"},
}


def cyr_to_lat(text: str, sep: str = "-") -> str:
    return sep.join(
        "".join(t.get(lett, lett) for lett in word) for word in text.lower().split()
    )


inputed = input()

print(cyr_to_lat(inputed))
print(cyr_to_lat(inputed, sep="+"))


# 5
def func1(body: str, tag: str = "h1") -> str:
    return f"<{tag}>{body}</{tag}>"


inputed = input()

print(func1(inputed))
print(func1(inputed, "div"))


# 6
def func2(body: str, tag: str = "h1", up: bool = True) -> str:
    if up:
        tag = tag.upper()

    return f"<{tag}>{body}</{tag}>"


inputed = input()

print(func2(inputed, tag="div"))
print(func2(inputed, tag="div", up=False))

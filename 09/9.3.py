# 1
nums = map(float, input().split())

print(*(next(nums) for _ in range(3)))


# 2
nums = map(lambda n: abs(int(n)), input().split())

print(*list(nums), end=" ")


# 3
import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))
lst2D = [*map(lambda line: [*map(int, line.split())], lst_in)]


# 4
s = input()
s_lst = s.split()
tp = tuple(map(lambda pair: tuple(pair.split("=")), s_lst))


# 5
t = {
    **{"ё": "yo", "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e"},
    **{"ж": "zh", "з": "z", "и": "i", "й": "y", "к": "k", "л": "l", "м": "m"},
    **{"н": "n", "о": "o", "п": "p", "р": "r", "с": "s", "т": "t", "у": "u"},
    **{"ф": "f", "х": "h", "ц": "c", "ч": "ch", "ш": "sh", "щ": "shch", "ъ": ""},
    **{"ы": "y", "ь": "", "э": "e", "ю": "yu", "я": "ya"},
}

print(*map(lambda char: t.get(char, "-"), input().lower()), sep="")


# 6
print(*map(lambda c: c if len(c) > 5 else "-", input().split()))

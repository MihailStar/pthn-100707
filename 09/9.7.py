# 1
rivers = input().split()

print(*sorted(rivers, key=len, reverse=True))


# 2
import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))
dct = {key: int(value) for key, value in (item.split("=") for item in lst_in)}

print(*sorted(dct, key=lambda k: dct[k], reverse=True))


# 3
notes = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
note_to_index = {note: index for index, note in enumerate(notes)}

print(*sorted(input().split(), key=lambda note: note_to_index[note]))


# 4
import sys
from typing import Iterable, List, Tuple, Union

lst_in = list(map(str.strip, sys.stdin.readlines()))
converters = (int, None, int, None)
indexs = (3, 0, 2, 1)
t_sorted: Iterable[Tuple[Union[int, str], ...]] = []

for y, line in enumerate(lst_in):
    items = line.split(";")
    row: List[Union[int, str]] = [i for i in range(len(items))]

    for x, value in enumerate(items):
        converter = converters[x]
        row[indexs[x]] = converter(value) if y > 0 and converter else value

    t_sorted.append(tuple(row))

t_sorted = tuple(t_sorted)


# 5
import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))
ranks = [
    *["рядовой", "сержант", "старшина", "прапорщик"],
    *["лейтенант", "капитан", "майор", "подполковник", "полковник"],
]
rank_to_index = {rank: index for index, rank in enumerate(ranks)}
lst = [[name, rank] for name, rank in (pair.split("=") for pair in lst_in)]

lst.sort(key=lambda name_and_rank: rank_to_index[name_and_rank[1]])

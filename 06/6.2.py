# 3
RU_TO_MORZE = {
    **{"А": ".-", "Б": "-...", "В": ".--", "Г": "--.", "Д": "-..", "Е": "."},
    **{"Ё": ".", "Ж": "...-", "З": "--..", "И": "..", "Й": ".---", "К": "-.-"},
    **{"Л": ".-..", "М": "--", "Н": "-.", "О": "---", "П": ".--.", "Р": ".-."},
    **{"С": "...", "Т": "-", "У": "..-", "Ф": "..-.", "Х": "....", "Ц": "-.-."},
    **{"Ч": "---.", "Ш": "----", "Щ": "--.-", "Ъ": "--.--", "Ы": "-.--", "Ь": "-..-"},
    **{"Э": "..-..", "Ю": "..--", "Я": ".-.-", " ": "-...-"},
}
inputed = input()

print(*(RU_TO_MORZE.get(char.upper(), char) for char in inputed))


# 4
MORZE_TO_RU = {
    **{".-": "А", "-...": "Б", ".--": "В", "--.": "Г", "-..": "Д", ".": "Е"},
    **{".": "Е", "...-": "Ж", "--..": "З", "..": "И", ".---": "Й", "-.-": "К"},
    **{".-..": "Л", "--": "М", "-.": "Н", "---": "О", ".--.": "П", ".-.": "Р"},
    **{"...": "С", "-": "Т", "..-": "У", "..-.": "Ф", "....": "Х", "-.-.": "Ц"},
    **{"---.": "Ч", "----": "Ш", "--.-": "Щ", "--.--": "Ъ", "-.--": "Ы", "-..-": "Ь"},
    **{"..-..": "Э", "..--": "Ю", ".-.-": "Я", "-...-": " "},
}
inputed = input().split()

print(*(MORZE_TO_RU.get(char, char).lower() for char in inputed), sep="")


# 5
print(*dict.fromkeys(input().split()).keys())


# 6
import sys
from typing import Dict, List

lst_in = list(map(str.strip, sys.stdin.readlines()))
day_to_names: Dict[int, List[str]] = {}

for record in lst_in:
    day, name = record.split()
    day_to_names[int(day)] = day_to_names.get(int(day), []) + [name]

for day, names in day_to_names.items():
    print(f"{day}:", end=" ")
    print(*names, sep=", ")


# 7
things = {
    **{"карандаш": 20, "зеркальце": 100, "зонт": 500, "рубашка": 300, "брюки": 1000},
    **{"бумага": 200, "молоток": 600, "пила": 400, "удочка": 1200, "расческа": 40},
    **{"котелок": 820, "палатка": 5240, "брезент": 2130, "спички": 10},
}
sorted_things = sorted(things.items(), key=lambda thing: thing[1], reverse=True)
n = int(input()) * 1_000
weight = 0

for thing in sorted_things:
    if weight + thing[1] > n:
        continue

    print(thing[0], end=" ")
    weight += thing[1]

# 2
num = int(input())

#     | ИЛИ
# 0 0 0
# 0 1 1
# 1 0 1
# 1 1 1

print(num | 0b1000)  # Включить по маске


# 3
num = int(input())

#     ~ НЕ
#   0 1
#   1 0

#     & И
# 0 0 0
# 0 1 0
# 1 0 0
# 1 1 1

print(num & ~0b10010)  # Выключить по маске с инверсией


# 4
num = int(input())

#     ^ исключающее ИЛИ
# 0 0 0
# 0 1 1
# 1 0 1
# 1 1 0

print(num ^ 0b1001)  # Переключить по маске


# 5
num = int(input())

print(num << 2)


# 6
num = int(input())

print(num >> 1)


# 7
encrypted_word = input()
key = 123

print(*(chr(ord(encrypted_char) ^ key) for encrypted_char in encrypted_word), sep="")


# 8
num = int(input())
mask = 0b1001000

print("ДА" if num & mask == mask else "НЕТ")  # Проверить включение по маске


# 9
num = int(input())

print(
    "ДА" if num & 0b10000 == 0b10000 or num & 0b10 == 0b10 else "НЕТ"
)  # Проверить включение по маскам

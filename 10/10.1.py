# 3
r = 2
print((1 * r**3) + (0 * r**2) + (1 * r**1) + (0 * r**0))  # -> 10


# 4
def convert_binary_to_decimal(num: int) -> int:
    radix = 2
    decimal = 0
    digs = str(num)
    for index in range(len(digs)):
        dig = digs[index]
        decimal += int(dig) * radix ** (len(digs) - 1 - index)
    return decimal


r = 2
print(convert_binary_to_decimal(101101))  # -> 45


# 6
from string import ascii_lowercase

r = 16
print(((10 + ascii_lowercase.index("a")) * r**1) + (9 * r**0))  # -> 169


# 7
from string import ascii_lowercase

r = 16
print(
    ((10 + ascii_lowercase.index("c")) * r**1)
    + ((10 + ascii_lowercase.index("f")) * r**0)
)  # -> 207


# 8
r = 8
print((1 * r**1) + (0 * r**0))  # -> 8


# 9
r = 8
print((5 * r**1) + (4 * r**0))  # -> 44

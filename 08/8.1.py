# 2
import math

print(math.ceil(float(input())))


# 3
from math import floor

print(floor(float(input())))


# 4
from math import factorial as fact


def factorial(n: int) -> int:
    p = 1
    for i in range(2, n + 1):
        p *= i
    print("my factorial")
    return p


# 5
from random import randint, seed

seed(1)
print(randint(10, 50))


# 6
from random import random as rnd
from random import seed

seed(10)
print(round(rnd(), 2))

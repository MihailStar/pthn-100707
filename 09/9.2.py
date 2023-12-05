# 1
from typing import Generator

N = int(input())


def get_sum(stop: int) -> Generator[int, None, None]:
    for num in range(1, stop + 1):
        yield sum(range(1, num + 1))


# 2
from typing import Generator


def balakirev(n: int) -> Generator[int, None, None]:
    three_of = [1, 1, 1]

    for num in three_of:
        yield num

    for _ in range(3, n):
        next = sum(three_of)
        three_of = [three_of[1], three_of[2], next]
        yield next


print(*balakirev(int(input())))


# 3
import random
import string
from typing import Generator

chars = string.ascii_lowercase + string.ascii_uppercase + "0123456789!?@#$*"
random.seed(1)


def get_password(length: int) -> Generator[str, None, None]:
    while True:
        password = ""
        for _ in range(length):
            password += chars[random.randint(0, len(chars) - 1)]
        yield password


gen = get_password(int(input()))

for _ in range(5):
    print(next(gen))


# 4
import random
import string
from typing import Generator

chars = string.ascii_lowercase + string.ascii_uppercase
random.seed(1)


def get_email(length: int) -> Generator[str, None, None]:
    while True:
        email = ""
        for _ in range(length):
            email += chars[random.randint(0, len(chars) - 1)]
        yield email + "@mail.ru"


gen = get_email(int(input()))

for _ in range(5):
    print(next(gen))


# 5
from typing import Generator


def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for divider in range(2, int(num**0.5) + 1):
        if num % divider == 0:
            return False
    return True


def prime_generator() -> Generator[int, None, None]:
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1


gen = prime_generator()

for _ in range(20):
    print(next(gen), end=" ")

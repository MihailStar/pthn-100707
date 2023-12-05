# 2
N = int(input())


def get_rec_N(n: int) -> None:
    if n < 1:
        return
    get_rec_N(n - 1)
    print(n)


# 3
from typing import List

nums = [int(d) for d in input().split()]


def get_rec_sum(ints: List[int]) -> int:
    if len(ints) < 2:
        return ints[0]
    return ints[0] + get_rec_sum(ints[1:])


print(get_rec_sum(nums))


# 4
from typing import List

N = int(input()) - 2


def fib_rec(N: int, f: List[int] = [1, 1]) -> List[int]:
    if N < 1:
        return f
    return fib_rec(N - 1, f + [f[-2] + f[-1]])


# 5
n = int(input())


def fact_rec(n: int) -> int:
    """@tutorial https://stepik.org/lesson/567058/step/6?discussion=5829169&unit=561332"""
    if n < 2:
        return 1
    return n * fact_rec(n - 1)


# 6
from typing import List, Optional, Union

Item = Union[int, float, bool, str]
RecursiveItem = Union[Item, List["RecursiveItem"]]

d: List[RecursiveItem] = [
    1,
    2,
    [True, False],
    ["Москва", "Уфа", [100, 101], ["True", [-2, -1]]],
    7.89,
]


def get_line_list(
    d: List["RecursiveItem"], a: Optional[List["Item"]] = None
) -> List[Item]:
    if a is None:
        a = []
    for item in d:
        if isinstance(item, list):
            get_line_list(item, a)
        else:
            a.append(item)
    return a


print(get_line_list(d))


# 7
N = int(input())


def get_path(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2

    return get_path(n - 1) + get_path(n - 2)


print(get_path(N))


# 8
from typing import List

nums = [int(d) for d in input().split()]


def merge(left: List[int], right: List[int]) -> List[int]:
    result: List[int] = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(nums: List[int]) -> List[int]:
    """@tutorial AI"""
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left_half = merge_sort(nums[:mid])
    right_half = merge_sort(nums[mid:])

    return merge(left_half, right_half)


print(*merge_sort(nums))

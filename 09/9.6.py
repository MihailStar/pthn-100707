# 2
s = input()
lst = list(map(int, s.split()))
lst.sort()
tp_lst = tuple(sorted(map(int, s.split())))


# 3
from typing import Dict, List


def get_sort(d: Dict[str, str]) -> List[str]:
    return [val for _key, val in sorted(d.items(), reverse=True)]


# 4
nums = map(int, input().split())

print(*sorted(set(nums), reverse=True)[:4])


# 5
nums_a = map(int, input().split())
nums_b = map(int, input().split())

print(
    *(
        num_a + num_b
        for num_a, num_b in zip(
            sorted(nums_a, reverse=False), sorted(nums_b, reverse=True)
        )
    )
)


# 6
import sys
from typing import Dict, List

lst_in = list(map(str.strip, sys.stdin.readlines()))
dct = dict(
    map(lambda item: (int(item[1]), item[0]), map(lambda pair: pair.split(":"), lst_in))
)


def foo(dct: Dict[int, str]) -> List[str]:
    return list(map(lambda item: item[1], sorted(dct.items())[:3]))


print(*foo(dct))

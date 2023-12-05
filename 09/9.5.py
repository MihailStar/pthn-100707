# 1
nums_a = map(int, input().split())
nums_b = map(int, input().split())
iterator = map(
    lambda num_a_and_num_b: num_a_and_num_b[0] * num_a_and_num_b[1], zip(nums_a, nums_b)
)

print(next(iterator), end=" ")
print(next(iterator), end=" ")
print(next(iterator), end=" ")


# 2
import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))
iterator = zip(*zip(*map(str.split, lst_in)))

for row in iterator:
    print(*row, sep=" ")


# 3
import sys

for row in zip(
    *((int(dig) for dig in line.strip().split()) for line in sys.stdin.readlines())
):
    print(*row)


# 4
words = input().split()

for y in range(0, len(words) - len(words) % 3, 3):
    print(*words[y : y + 3])


# 5
s = input()

lst = list(zip(s, range(10)))

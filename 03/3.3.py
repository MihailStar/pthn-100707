# 2
word = input()

print(word.title())


# 3
string = input().split("-")

print(len(string) - 1)


# 6
string = input()

print(string.find("ra"))


# 7
import re as regexp

string = input()

print(regexp.sub(r"-{2,}", "-", string))


# 8
print("\n".join(map(lambda digits: digits.zfill(3), input().split())))


# 9
print(input().count(" ") + 1)


# 10
print(";".join(input().split()))

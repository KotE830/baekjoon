import re

def func(s: str) -> bool:
    s = re.sub('->', '', s)
    return s == s[::-1]


print(func("1->2->2->1"))
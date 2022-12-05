x, y = input().split()
print(str(int(x[::-1]) + int(y[::-1]))[::-1].lstrip('0'))
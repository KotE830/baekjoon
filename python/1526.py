n = int(input())
result, i = 0, 1
while n > 0:
    if n % 10 >= 7:
        result = result + 7 * (10**i)
    else:
        result = result + 4 * (10**i)
    i = i + 1
    n = n % 10
    print(result)
print(result)
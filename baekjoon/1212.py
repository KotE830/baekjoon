print(bin(int(input(), 8))[2:])

'''
def toBinary(num: str) -> str:
    if num == '0':
        return num
    
    result = ''
    for i in num:
        n = int(i)
        divide = [4, 2, 1]
        for k in divide:
            if n >= k:
                n -= k
                result += '1'
            else:
                result += '0'

    return result.lstrip('0')


print(toBinary(str(input())))
'''
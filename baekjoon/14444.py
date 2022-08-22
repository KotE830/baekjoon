# equal to 13275

s = input().replace('', '#')
p, r = -1, -1
res = []

for i in range(len(s)):
    if i > r:
        p = r = i
        while r < len(s) and 2*p >= r and s[r] == s[2*p-r]: r += 1
        r -= 1
        res.append(r-p)
    else:
        j = 2*p - i
        if res[j] < r-i:
            res.append(res[j])
        elif res[j] > r-i:
            res.append(r-i)
        else:
            p = i
            while r < len(s) and 2*p >= r and s[r] == s[2*p-r]: r += 1
            r -= 1
            res.append(r-p)

print(max(res))
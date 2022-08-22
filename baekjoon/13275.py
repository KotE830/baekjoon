# equal to 14444

s = input().replace('', '#')
p, r = -1, -1
l = len(s)
res = []

for i in range(l):
    if i > r:
        p = r = i
        while r < l and r <= 2*p and s[r] == s[2*p-r]:
            r += 1
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
            while r < l and r <= 2*p and s[r] == s[2*p-r]:
                r += 1
            r -= 1
            res.append(r-p)

print(max(res))
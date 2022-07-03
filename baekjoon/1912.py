n = int(input())
nums = list(map(int, input().split()))

sums = 0
li = []
for i in nums:
    if i > 0:
        sums = sums + i
    elif i < 0:
        if sums > 0:
            li.append(sums)
        li.append(i)
        sums = 0
if sums > 0:
    li.append(sums)

result = li[0]
min, max = 0, 0
print(li)

for i in range(len(li)):
    print(sum(li[:i+1]))
    if li[i] > 0 and result < sum(li[:i+1]):
        result = sum(li[:i+1])
        print(result, "I")
        max = i+1
        
for i in range(max):
    print(sum(li[i:max]))
    if li[i] > 0 and result < sum(li[i:max]):
        result = sum(li[i:max])
        print(result, "I")
        min = i

print(result)
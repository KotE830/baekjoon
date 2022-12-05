A, B = input().split()
i, min_cnt = 0, len(A)

while i <= len(B)-len(A):
    cnt = 0
    for j in range(len(A)):
        if A[j] != B[i+j]:
            cnt += 1
    if min_cnt > cnt:
        min_cnt = cnt
    i += 1

print(min_cnt)
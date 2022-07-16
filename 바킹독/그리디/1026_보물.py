# 보물

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
result = []

A.sort()
B.sort(reverse=True)

for i in range(N):
    result.append(A[i]*B[i])

print(sum(result))
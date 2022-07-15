# 정수 삼각형
# 이전의 RGB 거리와같은 방식으로??
import sys

N = int(input())
bucket = []
sumBucket = [[0 for _ in range(i)] for i in range(1, N+1)]

for _ in range(N):
    floor = list(map(int, sys.stdin.readline().split()))
    bucket.append(floor)

sumBucket[0][0] = bucket[0][0]

for i in range(1, N):
    sumBucket[i][0] = sumBucket[i-1][0] + bucket[i][0] # 가장 앞
    sumBucket[i][-1] = sumBucket[i-1][-1] + bucket[i][-1] # 가장 뒤
    for j in range(1, i):
        sumBucket[i][j] = max(sumBucket[i-1][j-1], sumBucket[i-1][j]) + bucket[i][j] # 가장 앞과 가장 뒤를 제외한 가운데

print(max(sumBucket[N-1]))


## 다른 사람 풀이1 길이가 293B 로 나의 516B 보다 223B적다..
import sys

N = int(sys.stdin.readline())
arr = []
for i in range(0, N):
    arr.append(list(map(int, sys.stdin.readline().split())))

for i in range(N - 1, 0, -1):
    for j in range(0, len(arr[i]) - 1):
        arr[i - 1][j] = max(arr[i][j], arr[i][j + 1]) + arr[i - 1][j]

print(arr[0][0])
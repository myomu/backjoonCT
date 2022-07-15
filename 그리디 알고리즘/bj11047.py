# 동전 0

N, K = map(int, input().split())
values = []
for _ in range(N):
    values.append(int(input()))

checkPoint = N-1
targetNum = K
cnt = 0

while True:
    if targetNum == 0 or checkPoint == -1:
        break
    if targetNum / values[checkPoint] >= 1:
        count = targetNum // values[checkPoint]
        cnt += count
        targetNum -= count * values[checkPoint]
        #print(f'cnt={cnt}, targetNum={targetNum}, checkPoint={checkPoint}')
    else:
        checkPoint -= 1
print(cnt)


## 다른 사람 풀이
import sys

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

A = []
for i in range(N):
    A.append(int(input().rstrip()))

A.sort(reverse=True)
cnt = 0
for i in A:
    if i <= K:
        cnt += K // i
        K = K % i
    if not K:
        break

print(cnt)
# RGB거리
# 두고두고 보면 좋을듯..! 재귀 방식과 반복문 방식 두 가지 방식이 존재한다. 아래는 반복문으로 푼 것.

import sys

N = int(input())
bucket = []
sumList = [[0 for _ in range(3)] for _ in range(N)]

for _ in range(N):
    R, G, B = map(int, sys.stdin.readline().rstrip().split())
    bucket.append([R, G, B])

sumList[0][0] = bucket[0][0]
sumList[0][1] = bucket[0][1]
sumList[0][2] = bucket[0][2]

for i in range(1, N):
    sumList[i][0] = min(sumList[i-1][1], sumList[i-1][2]) + bucket[i][0]
    sumList[i][1] = min(sumList[i-1][0], sumList[i-1][2]) + bucket[i][1]
    sumList[i][2] = min(sumList[i-1][0], sumList[i-1][1]) + bucket[i][2]

print(min(sumList[N-1]))
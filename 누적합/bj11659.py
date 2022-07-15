# 구간 합 구하기 4
# 시간 초과가 발생하는 문제인 것 같다.. 단순하게 풀면 시간 초과가 나올 것으로 보이므로..
# 누적합 문제라고 하였음으로..
# 1부터 리스트를 쭉 더하고 최소값 bottom아래의 구간 합을 빼면 될 것 같다.

import sys

N, M = map(int, input().split())
li = list(map(int, sys.stdin.readline().split()))
sumNumbers = [0]*(N+1)
sumNumbers[1] = li[0]

for i in range(2, N+1):
    sumNumbers[i] = li[i-1] + sumNumbers[i-1]
#print(sumNumbers)
for i in range(M):
    bottom, top = map(int, sys.stdin.readline().split())
    print(sumNumbers[top] - sumNumbers[bottom-1])

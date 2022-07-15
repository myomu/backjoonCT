# 연속합

# 모든 값이 음수일 경우가 문제가 된다.
# 그러나 먼저 sumValue가 maxValue보다 크다면 maxValue에 sumValue의 값을 넣는 if문을 먼저 오게 하면
# 가장 큰 음수를 maxValue에 넣을 수 있다.

import sys

maxValue = -1000
sumValue = 0

N = int(input())
numbers = list(map(int, sys.stdin.readline().split()))

for number in numbers:
    sumValue += number

    if sumValue > maxValue: # 이 if문이 먼저오면 모든 값이 음수일 경우 가장 큰 음수를 maxValue에 넣게 된다.
        maxValue = sumValue

    if sumValue < 0: # sumValue가 음수가 되면 항상 sumValue를 0으로 초기화 시킨다.
        sumValue = 0 # 이렇게 하는 이유는 음수가 되면 앞의 숫자를 계속 더해온 값이 쓸모없기 때문이다. 2 3 -6 7..이럴때 2+3-6은 쓸모 없게된다.
        # 그러므로 처음부터 다시 더해가는 초기화를 하는 것이다.

print(maxValue)
    

# 다른 사람 풀이 리스트를 이용했음.
from sys import stdin, stdout
n = int(stdin.readline())
DP = list(map(int, stdin.readline().split()))
for i in range(1, n):
    DP[i] = max(DP[i], DP[i] + DP[i-1])
print(max(DP))
# 가장 긴 증가하는 부분 수열

import sys

N = int(input())
A = list(map(int, sys.stdin.readline().split()))
dp = [1]*1001

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+1) # dp[i]와 dp[j]+1 을 비교하여 큰 수를 넣어준다. 모든 수를 비교. O(n^2)
            # dp[j]의 값이 j에 따라 변함으로 그중 가장 큰 수를 찾기 위해 dp[i]를 비교하는 것이다.
            # dp[i]는 maxValue 라는 변수라고 생각해도 무방하다.
            # +1의 이유는 앞의 오름차순의 끝 수보다 크기에 카운트를 하나 더 해주는 것.

print(max(dp)) # dp 중 가장 큰 값을 찾는다. 즉, 오름차순의 길이가 가장 긴 것을 찾는 것.
            
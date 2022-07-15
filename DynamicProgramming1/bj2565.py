# 전깃줄
# 이전의 Longest Increase Sequence(LIS) 문제와 유사하다. 11053, 11054
# 증가하는 부분으로 최대값을 구하고 전체 길이 - 최대값 하면 없애야할 전깃줄의 최소값이 나올 것이다.

import sys

input = sys.stdin.readline
lis = [0]*501
N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    lis[a] = b

dp = [1]*501
for i in range(1, 501):
    for j in range(1, i):
        if lis[j] == 0: # 아래의 주석에서 말한대로 문제가 발생하여 이 조건을 추가.
                        # lis[j] 가 0인 경우 아래 비교문을 실행시키지 않는다.
            continue
        if lis[i] > lis[j]:
            dp[i] = max(dp[i], dp[j]+1) #여기서 증가하는 오름차순 부분 수열을 구한다.
                                        #단, 0인 경우는 dp에 추가하지 않도록..
                                        # lis[i]가 0인 경우 0도 오름차순에 포함시켜 길이를 측정하게된다..문제발생!
                                        # 왜냐하면 B의 값에는 0이 존재하지 않기 때문.
                                        # 1~500 사이의 자연수가 겹치지 않도록 주어지기 때문이다.
print(N-max(dp))



## 다른 사람 풀이
# 이 경우 이중 배열로 리스트를 만들어서 0의 조건을 없앴다.
# 그냥 정렬로 오름차순으로 만듦.
import sys

input = sys.stdin.readline
N = int(input())

lineList = []

for _ in range(N):
    lineList.append(list(map(int, input().rstrip('\n').split())))

lineList.sort()

# 0번째 인덱스에 대해 정렬을 하면
# 가장 긴 증가하는 순열을 구하는 방법이랑 똑같게 됨 : dp의 각 숫자는 자기 인덱스의 값이 꼭 포함되는 방식임!
dp = [1]*N
for i in range(N):
    for j in range(i):
        if lineList[i][1] > lineList[j][1] and dp[i] < dp[j]+1:
            dp[i] = dp[j] + 1

print(N-max(dp))
# 나머지 합

# 요 방식으로도 답은 구해지지만 O(N^2)의 시간복잡도를 가짐으로 시간초과가 나오게 된다.
# import sys

# input = sys.stdin.readline
# N, M = map(int, input().split())
# seq = list(map(int, input().split()))
# sumSeq = [0]*(N+1)
# sumSeq[1] = seq[0]

# for i in range(2, N+1):
#     sumSeq[i] = sumSeq[i-1] + seq[i-1]

# cnt = 0
# for i in range(1, N+1):
#     for j in range(i, N+1):
#         diff = sumSeq[j] - sumSeq[j-i]
#         if diff%3 == 0:
#             cnt += 1
#             #print(f'diff={diff} sumSeq[j]={sumSeq[j]}')

# print(cnt)

## 단순 반복이 아닌 누적합의 나머지를 통해 답을 구할 수 있다.
# 또한 나머지가 0이 아닌 것들 중 나머지가 동일한 것들의 조합combination을 통해 일정 범위내의 나머지가 0이 되는 것을 구할 수 있다.
# 예를 들어 3으로 나눠지는 것을 구할 때  1 2 3 1 2 6 여기서 누적합은 1 3 6 7 9 15 이다. 1과 7은 나머지가 1이다.
# 그런데 7-1을 하면 합이 6이 됨으로 3으로 나눠지게 된다. 이처럼 나머지가 동일한 것들의 조합으로 나머지가 0이 되는
# 것들을 구할 수 있다. 9-6=3 처럼 3으로 나눠지는 나머지가 0인 것들의 조합도 구해야한다.

import sys

input = sys.stdin.readline
N, M = map(int, input().split())
seq = list(map(int, input().split()))
sumSeq, cnt = 0, 0
rOfSum = [0 for _ in range(M)]

for i in range(N):
    sumSeq += seq[i]
    r = sumSeq%M
    if r == 0:
        cnt += 1
    rOfSum[r] += 1

for i in range(M):
    cnt += rOfSum[i]*(rOfSum[i]-1) // 2 # 한 수가 홀수면 -1을 통해 한 수는 짝수가 됨으로 항상 자연수를 유지한다. // 사용

print(cnt)
# 1 3 6 7 9
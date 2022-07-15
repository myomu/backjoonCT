# 수열
import sys

N, K = map(int, input().split())
seq = list(map(int, sys.stdin.readline().split()))
sumSeq = [seq[0]]

for i in range(1, N):
    sumNumber = seq[i] + sumSeq[i-1]
    sumSeq.append(sumNumber)

sumSeqK = [sumSeq[K-1]] # 처음 합하는 연속된 수는 이전 값을 뺄 것이 없기에 리스트에 넣어주고
# 이후 K 번째 부터 앞에 뺄 것이 존재하기 때문에 아래 for문의 식을 사용한다.
for j in range(K, N):
    sumSeqK.append(sumSeq[j] - sumSeq[j-K])

print(max(sumSeqK))


## 다른 사람 풀이
def solve(n, k, A):
    opt = S = sum(A[:k])
    for i in range(n - k):
        S = S - A[i] + A[i + k] # 이 부분이 핵심인듯.
        opt = max(opt, S)
    return opt

import sys
input = sys.stdin.readline
n, k = map(int, input().split())
A = list(map(int, input().split()))
print(solve(n, k, A))
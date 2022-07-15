# 가장 긴 바이토닉 부분 수열
# bj11053 의 원리와 비슷하다
# 단지 증가와 감수 부분을 나누어 생각해야하고
# i 가 기준이 되어 증가와 감소의 구분점이 된다. 이 둘의 조합을 합한 것의 최대값이 답이 된다.

import sys

input = sys.stdin.readline
N = int(input())
S = list(map(int, input().split()))
reverse_S = S[::-1]
inc = [1]*N
dec = [1]*N
ans = [0]*N

for i in range(N):
    for j in range(i):
        if S[i] > S[j]:
            inc[i] = max(inc[i], inc[j]+1)
        if reverse_S[i] > reverse_S[j]:
            dec[i] = max(dec[i], dec[j]+1)

# 다시 dec.reverse()를 사용해 뒤집는 경우도 있지만 결국은 N-i-1(N은 길이임으로 위치는 -1을 해줘야함.)이
# 반대되는 decrease의 위치인셈. 9라는 길이의 자에서 5를 기준으로 나누면 5, 4 이렇게 되는 원리.

for i in range(N):
    ans[i] = inc[i] + dec[N-i-1] - 1

print(max(ans))

# 포도주 시식
# 경우의 수를 나열해보면 법칙을 발견할 수 있다.
# 이전의 포도주를 먹는 경우와 아닌경우, 이번 포도주를 안먹는 겨우 3가지의 경우의 수로 나누어 생각한다.
# https://myjamong.tistory.com/313 참고
# N = 1 일 때 런티임 에러가 나온다..dp[2] = d[1] + d[2] 의 경우 dp[2]가 존재하지 않아서 생김.
import sys

N = int(input())
d = [0]*(N+2) #d[2] 때문에 +1이 아닌 +2로 설정.
dp = [0]*(N+2) #dp[2] 때문에 +1이 아닌 +2로 설정.

for i in range(1, N+1):
    d[i] = int(sys.stdin.readline().strip())
    
dp[1] = d[1]
dp[2] = d[1] + d[2]

for i in range(3, N+1):
    dp[i] = max(dp[i-1], dp[i-2]+d[i], dp[i-3]+d[i-1]+d[i])

print(dp[N])
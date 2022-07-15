# 계단 오르기

# d와 route의 범위를 입력값에 따라 메모리 용량을 처음에 조절했었는데 이후에 런타임에러가 떴었다..
# 입력 범위인 300 을 초과하는 301로 메모리를 이미 잡고 시작하였을 때 에러가나지 않았다.
import sys

N = int(input())
d = [0 for _ in range(301)]
route = [0 for _ in range(301)]
for i in range(N):
    d[i] = int(sys.stdin.readline().rstrip())

route[0] = d[0]
route[1] = route[0] + d[1]
route[2] = max(route[0], d[1]) + d[2]
for i in range(3, N):
    route[i] = max(route[i-3]+d[i-1], route[i-2]) + d[i]

print(route[N-1])
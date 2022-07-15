# 이항 계수2
# 이항 계수의 성질과 메모제이션 기법 사용을 요구한다. & 파스칼의 삼각형.
# 참고 https://guccin.tistory.com/52
# 참고2 https://shoark7.github.io/programming/algorithm/3-ways-to-get-binomial-coefficients

N, K = map(int, input().split())
bucket = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N+1):
    bucket[i][i] = 1
    bucket[i][0] = 1
for A in range(2, N+1):
    for B in range(1, K+1):
        bucket[A][B] = bucket[A-1][B] + bucket[A-1][B-1]

print(bucket[N][K]%10007)



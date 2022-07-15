# 다리 놓기
# 조합 방식을 이용. combination 모듈 사용했을 때 시간초과가 떳음.
# 앞서 이항계수2 문제의 코드를 사용하였다. 추훈 더 고민해볼것.

T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    bucket = [[0 for _ in range(M+1)] for _ in range(M+1)]
    for i in range(1, M+1):
        bucket[i][i] = 1
        bucket[i][0] = 1
    for A in range(2, M+1):
        for B in range(1, N+1):
            bucket[A][B] = bucket[A-1][B] + bucket[A-1][B-1]
    print(bucket[M][N])




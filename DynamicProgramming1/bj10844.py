# 쉬운 계단 수
# https://cotak.tistory.com/12 풀이 참고.

MOD = 1000000000
N = int(input())

d = [[0]*10 for _ in range(N+1)]
d[1] = [0] + [1 for _ in range(1, 10)]

for i in range(2, N+1):
    for j in range(10):
        if j == 9:
            d[i][j] = d[i-1][j-1]
        elif j == 0:
            d[i][j] = d[i-1][1] # 10 101 1210 1010 
        else:
            d[i][j] = d[i-1][j-1] + d[i-1][j+1] # 앞자리가 1인 경우 d[2][1] = d[1][0] + d[1][2] 이다.
            # d[1][0] 이 문제가 되는데 위의 j == 0 조건이 없으면 뒷자리수가 0이 되는 경우를 제외하게 된다.
            # 10 101 1010 1012 1210 등..

print(sum(d[N])%MOD)
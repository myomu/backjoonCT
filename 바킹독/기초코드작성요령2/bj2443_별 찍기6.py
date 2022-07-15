# 별 찍기 - 6

N = int(input())
for i in range(N):
    print(' '*i + '*'*(2*(N-i)-1))
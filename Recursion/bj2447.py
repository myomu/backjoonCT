# 별 찍기 - 10

# 이 방법을 사용했지만 시간초과.. 과도한 호출이 문제라고 하는듯?
# import sys
# print = sys.stdout.write

# n = int(input())

# def star(x, y, N):
#     if N/3 < x < N/3*2+1 and N/3 < y < N/3*2+1:
#         return 0
#     else:
#         if N == 3:
#             return 1
#         else:
#             return star(x%(N//3), y%(N//3), N//3)

# for i in range(1, n+1):
#     str = ''
#     for j in range(1, n+1):
#         if star(i, j, n):
#             str += '*'
#         else:
#             str += ' '
#     print(str + '\n')


## 두번 째 방법 시도...틀을 만들고 거기에 리스트를 변경하는 방식으로(x)
# 다른 사람 풀이 참조
import sys

def star(x, y, N):
    div = N//3
    if N == 1:
        bucket[x][y] = '*'
        return
    for i in range(3):
        for j in range(3):
            if i != 1 or j != 1:
                star(x+N//3*i, y+N//3*j, div)

n = int(input())
bucket = [[' ']*n for _ in range(n)]
print = sys.stdout.write

star(0, 0, n)

for i in range(n):
    for j in range(n):
        print(bucket[i][j])
    print('\n')

# ctrl+Z 로 넣으면 EOFError 가 뜬다. input()은 그러하고 sys.stdin.readline()은 EOFError가 안뜬다.
# import sys
# while True:
#   a = sys.stdin.readline().rstrip() # input()
#   if a != '':
#     print(a)
#   else:
#     break


# a = 100
# b = a >> 1

# print(b)

# c = a >> 2
# print(c)
# from collections import deque
# li = [50, 160, 30, 60, 20, 100]
# li = deque(li)
# for i in range(6):
#     print(li)
#     li.rotate(-1)


n, m = map(int, input().split())
matrix = []
result = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(2*n):
    matrix.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        result[i][j] = matrix[i][j] + matrix[i+n][j]

for k in result:
    print(*k)


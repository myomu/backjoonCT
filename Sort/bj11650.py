# 좌표 정렬하기 왜 이중 리스트 min이 앞의 값을 우선시하여 찾는지?? 궁금함.
# sort, 또는 sorted 함수에 대해 좀더 공부해보기.
# lamda? 사용법 정렬의 기준 또는 sort함수의 로직 공부해보면 좋을듯

import sys

N = int(input())
coordinate = []

# x, y = map(int, sys.stdin.readline().split())
# coordinate.append([x, y])

# for i in range(N-1):
#     x, y = map(int, sys.stdin.readline().split())
#     for j in range(len(coordinate)):
#         if x > coordinate[j][0]:
#             coordinate.append([x, y][0])
#     coordinate.append([x, y])


for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    coordinate.append([x, y])
coordinate.sort()

for j in coordinate:
    print(j[0], j[1])

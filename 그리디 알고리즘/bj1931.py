# 회의실 배정
# https://www.acmicpc.net/board/view/81289#post 반례 존재
# 반례 고려하여 시작시간도 오름차순으로 정렬 조건 추가함.

import sys

input = sys.stdin.readline

N = int(input())
timeTable = []
for _ in range(N):
    timeTable.append(list(map(int, input().split())))

timeTable.sort(key=lambda x: (x[1], x[0])) # 시작시간 후순위 조건.
print(timeTable)
endTime = -1
cnt = 0
for i in timeTable:
    if i[0] >= endTime:
        cnt += 1
        endTime = i[1]

print(cnt)

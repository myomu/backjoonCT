# 나이순 정렬

import sys

n = int(input())
memberList = []

for i in range(n):
    age, name = sys.stdin.readline().split()
    memberList.append([int(age), name, i])
sortMemberList = sorted(memberList, key= lambda x:(x[0], x[2]))

for j in sortMemberList:
    print(j[0], j[1])
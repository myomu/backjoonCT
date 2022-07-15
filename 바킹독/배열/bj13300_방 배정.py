# 방 배정

import math

man = [0 for _ in range(7)]
woman = [0 for _ in range(7)]

N, K = map(int, input().split())
for _ in range(N):
    gender, grade = map(int, input().split())
    if gender == 0:
        woman[grade] += 1
    else:
        man[grade] += 1

for i in range(1, 7):
    woman[i] = math.ceil(woman[i]/K)
    man[i] = math.ceil(man[i]/K)

print(sum(woman) + sum(man))
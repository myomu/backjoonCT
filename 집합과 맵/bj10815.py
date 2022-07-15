# 숫자 카드
import sys

N = int(input())
card = list(map(int, sys.stdin.readline().split()))
M = int(input())
findCard = list(map(int, sys.stdin.readline().split()))
dic = dict()

for i in card:
    dic[i] = 1
for j in findCard:
    findValue = dic.get(j, 0)
    print(findValue, end=' ')
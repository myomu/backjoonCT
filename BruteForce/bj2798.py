# 블랙잭

# 1. 단순 무식 for문 세 번 반복..;; 일단 통과는 된다.
import sys

N, M = map(int, input().split())

cardList = list(map(int, sys.stdin.readline().split()))
# print(cardList)

maxNum = 0
for one in cardList:
    for second in cardList:
        if second == one:
            continue
        for third in cardList:
            if third == second or third == one:
                continue
            sumNumber = one + second + third
            if sumNumber > maxNum and sumNumber <= M:
                maxNum = sumNumber
            # print(one, second, third, 'maxNum=', maxNum, 'sumNumber=', sumNumber)
print(maxNum)

# 더 효율 좋은 방법 1
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a=list(map(int,input().split()))
def combination(arr, k):
    if k==1:
        return arr
    l=[]
    for i in range(len(arr)-k+1):
        m=arr[i]
        sub_arr=arr[i+1:]
        for j in combination(sub_arr,k-1):
            l.append(m+j)
    return l
print(max([i for i in combination(a,3) if i<=m]))

# 더 좋은 방법 2 파이썬 모듈 combination 이용
from itertools import combinations
N, M = map(int, input().split())
lst = list(map(int, input().split()))
results = []
for i in combinations(lst, 3):
    if sum(i) <= M:
        results.append(sum(i))

print(max(results))
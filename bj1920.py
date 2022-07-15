# 수 찾기
import sys

N = int(input())
dic = dict()

num1 = list(map(int, sys.stdin.readline().split()))

M = int(input())
num2 = list(map(int, sys.stdin.readline().split()))

for i in num1:
    dic[i] = 1

for j in num2:
    #if j in dic: # 키를 찾는 이 방식은 O(N)의 시간 복잡도를 가진다 위의 for 문도 함치면 O(N^2)의 시간 복잡도가 될것..
    #    print(1)
    if dic.get(j) != None: # get을 통해 해당 키가 있는지 체크하면 O(N)의 시간 복잡도를 가진다.
        print(1)
    else:
        print(0)
# print(dic)
# print(dic[7])
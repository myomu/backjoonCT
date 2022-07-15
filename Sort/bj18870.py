# 좌표 압축
import sys

N = int(input())
coordinate = list(map(int, sys.stdin.readline().split()))
setLi = set(coordinate)
sortLi = sorted(list(setLi))
dic = {}
for i in range(len(sortLi)):
    dic[sortLi[i]] = i

for j in coordinate:
    print(dic[j], end=' ')

## 다른 사람의 더 짧은 코드. 방식은 비슷
import sys

def a():
    a=int(input())
    b=list(map(int,sys.stdin.readline().split()))
    c=list(sorted(set(b)))
    c={c[i]:i for i in range(len(c))} # 딕셔너리 타입으로 for문을 돌면서 딕셔너리 생성.
    print(*[c[i] for i in b]) # 리스트 앞에 asterisk(*)를 붙여서 unpacking 하여 순차 출력시킴.
    
a()
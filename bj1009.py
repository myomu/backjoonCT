# 분산처리 제곱은 뒤의 수가 일정한 수를 반복하는 성질을 지닌다.
# 1 - 1, 1, 1, 1, if a == 1: print(1)
# 2 - 2, 4, 8, 16, 32, 64 128,...[2, 4, 8, 6, ...] li[b%4]
# 3 - 3, 9, 27, 81, 243, ... [3, 9, 7, 1, ...]
# 4 - 4, 16, 64, 256, 1024, ... [4, 6, 4, 6, ...]
# 5 - 5, 25, 125, ... [5, 5, 5, ...
# 6 - 6, 36, 216, 1296 ... [6, 6, 6,...
# 7 - 7, 49, 343, 2401, 16307, 117649... [7, 9, 3, 1, 7, 9, ...]
# 8 - 8, 64, 512, 4096, 32768...[8, 4, 2, 6]
# 9 - 9, 81, 729, 6561, ... [9, 1, 9, 1, ...
# 10 - 10, 100, 1000, ...[10, 10, 10]
# 11 - 11, 121, 1331, ...[1, 1, 1,...
# 12 - 12, 144, 1728, 20736, ... [2, 4, 8, 6,...]


import sys

T = int(input())
for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    li = []
    if a%10 == 0:
        print(10)
        continue
    if a%10 == 1 or a%10 == 5 or a%10 == 6:
        print(a%10)
        continue
    if a%10 == 2:
        li = [2, 4, 8, 6]
    if a%10 == 3:
        li = [3, 9, 7, 1]
    if a%10 == 4:
        li = [4, 6]
    if a%10 == 7:
        li = [7, 9, 3, 1]
    if a%10 == 8:
        li = [8, 4, 2, 6]
    if a%10 == 9:
        li = [9, 1]
    print(li[(b-1)%len(li)])


# 다른 사람 풀이1
t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    b=b%4+4
    number=a**b%10
    if number==0: print(10)
    else : print(number)

# 다른 사람 풀이 2
import sys 
input = sys.stdin.readline

t = int(input())
for _ in range(t):
	a,b = map(int,input().split())
	aa=a%10

	if aa == 0: # 패턴 1
		print(10)
	elif aa in [1,5,6]: 
		print(aa)
	elif aa in [4,9]: #패턴 2
		bb=b%2
		if bb == 0:
			print(aa*aa%10)
		else:
			print(aa)
	else: #패턴 4
		bb=b%4  
		if bb ==0:
			print(aa**4%10)
		else:
			print(aa**bb%10)
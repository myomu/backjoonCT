# 골드바흐의 추측
import sys

N = 10000
prime = [False, False] + [True] * (N-1)

for i in range(2, int(N**0.5)+1):
    if prime[i]:
        for j in range(i*2, N+1, i):
            prime[j] = False

t = int(sys.stdin.readline().rstrip())
for i in range(t):
    n = int(sys.stdin.readline().rstrip())
    firstHalf = []
    secondHalf = []

    for p in range(2, n+1):
        if prime[p]:
            if p <= n//2:
                firstHalf.append(p)
            if p >= n//2:
                secondHalf.append(p)

    for one in range(len(firstHalf)-1, -1, -1):
        breakpoint = True
        for two in range(len(secondHalf)):     
            if firstHalf[one]+secondHalf[two] == n:
                print(firstHalf[one], secondHalf[two])
                breakpoint = False
                break
        if breakpoint == False:
            break


## 다른 사람 풀이

arr=[False,False,True]+[True,False]*5000 # 2의 배수는 처음부터 False로 설정
for i in range(3,101,2): # 그래서 3부터 100까지 홀수인 것만 파악. 3, 5, 7,... 101인 이유는 (10000**0.5)+1 인듯
    if arr[i]: # 그것중 참인 것들 이전에 홀수는 전부 참이므로 조건에 해당
        arr[i*2::i]=[False]*len(arr[i*2::i]) # ::i는 i의 단위로 건너뛰어 리스트를 선택하는 것
                                            # i가 3이면 6부터 시작해서 6, 9, 12, ... 전부 False로 변경.
                                            # 그리고 [False]에 곱해주는 이유는 선택된 리스트의 요소들에 집어넣는 요소의 수가 같아야하기 때문이다.
import sys
input=sys.stdin.readline # 이렇게하면 아래에서 그냥 input()으로만 표현해도 되나봄?
t=int(input())
for i in range(t):
    n=int(input())
    m=n//2
    while m>0:
        if arr[m]==True and arr[n-m]==True:
            print(m,n-m)
            break
        else:
            m-=1

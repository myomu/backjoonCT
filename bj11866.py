# 요세푸스 문제 0

from collections import deque

N, K = map(int, input().split())
deq = deque([i for i in range(1, N+1)])
bucket = []

while len(deq):
    deq.rotate(-(K-1))
    bucket.append(deq.popleft())
    
print('<'+', '.join((map(str, bucket)))+'>')


## 다른 사람이 푼 문제 deque를 사용하지 않고 풀었다.
N,K=map(int,input().split())
ml=list(range(1,N+1))
dili=[]
n=0
for i in range(N):
    n+=K-1 ##
    if n>=len(ml): ##
        n=n%len(ml) ## 이부분이 이해 안간다.
    dili.append(str(ml.pop(n)))
print('<',', '.join(dili),'>',sep='')
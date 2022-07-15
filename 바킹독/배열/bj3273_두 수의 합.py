# 두 수의 합
# 난 dictionary를 이용해 풀었지만 포인터 즉, 앞과 뒤의 합으로 구하는 방법이 일반적이다.

n = int(input())
seq = sorted(list(map(int, input().split())))
x = int(input())
cnt = 0
diction = dict()

for i in seq:
    diction[i] = 1

for j in seq:
    if diction.get(x-j, 0):
        cnt += 1

print(cnt//2)
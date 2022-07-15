# 분해합

N = input()

numCount = len(N)
li = []
if int(N) >= 100:
    baseNumber = int(N) - 9*numCount
else:
    baseNumber = 1

for i in range(baseNumber, int(N)):
    numToStr = str(i)
    ctor = i
    for j in numToStr: # sum(map(int, str(i))) 이런식으로 합할 수도 있다. list로 sum함수를 통해 합을 구한다.
        ctor += int(j)
    if ctor == int(N):
        li.append(i)

if len(li) == 0:
    print(0)
else:
    print(min(li))


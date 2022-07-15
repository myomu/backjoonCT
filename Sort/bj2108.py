# 통계학

from collections import Counter
import sys, math
input = sys.stdin.readline
N = int(input())
bucket = []
for i in range(N):
    number = int(input())
    bucket.append(number)
bucket.sort()
arithmeticMean = sum(bucket)/N
median = bucket[math.ceil(N/2)-1]
mode = Counter(bucket).most_common()
rangeValue = max(bucket)-min(bucket)

resultMode = 0
if len(mode) == 1:
    resultMode = mode[0][0]
else:
    if mode[0][1] == mode[1][1]:
        resultMode = mode[1][0]
    else:
        resultMode = mode[0][0]

print(round(arithmeticMean))
print(median)
print(resultMode)
print(rangeValue)


# 다른 사람 풀이 Counter를 사용하지 않고 최빈값을 구함
import sys
n = int(sys.stdin.readline())
a = []
for i in range(n):
    m = int(sys.stdin.readline())
    a.append(m)
a.sort()
d = {}
for i in a:
    if i not in d:
        d[i] = 1
    else:
        d[i] = d[i] + 1

b = filter(lambda x:max(d.values())==x[1],d.items())
lst = []
for i, j in b:
    lst.append(i)


print(round(sum(a)/n))
print(a[n//2])
if len(lst) == 1:
    print(lst[0])
else:
    print(lst[1])
print(a[-1]-a[0])
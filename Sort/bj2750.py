# 수 정렬하기

n = int(input())

li = []
for i in range(n):
    num = int(input())
    li.append(num)

for j in range(len(li)):
    minnum = li[j]
    for k in range(j, len(li)):
        if li[k] < minnum:
            minnum = li[k]
            li[k] = li[j]
            li[j] = minnum           
        
for _ in li:
    print(_)
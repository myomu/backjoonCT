# 소트인사이드

N = input()

li = []
for i in N:
    li.append(int(i))
li.sort(reverse=True)
for j in li:
    print(j, end='')
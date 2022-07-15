# 애너그램 만들기

li1 = [0 for _ in range(26)]
li2 = [0 for _ in range(26)]

s1 = input()
s2 = input()
for i in s1:
    li1[ord(i)-97] += 1
for j in s2:
    li2[ord(j)-97] += 1

cnt = 0
for k in range(26):
    cnt += abs(li1[k] - li2[k])
print(cnt)
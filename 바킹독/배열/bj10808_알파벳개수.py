# 알파벳 개수

para = input()
bucket = [0 for i in range(26)]
for i in para:
    a = ord(i)-97
    bucket[a] += 1

print(*bucket)
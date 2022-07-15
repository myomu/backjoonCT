# Hashing

N = int(input())
strings = input()
hashingNum = 0
M = 1234567891

for i in range(N):
    num = ord(strings[i])-96
    hashingNum += num*(31**i)

print(hashingNum%1234567891)
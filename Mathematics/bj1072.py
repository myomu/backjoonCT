# 나누기

# 아하..ㅋㅋ;; 문제를 제대로 못 읽어서 계속 틀리다고 나온 거였음.
# N%F == 0 이 조건은 문제에 없는 것이다..
N = input()
F = int(input())
num = int(N[:-2]+'00')
#count = 0

for i in range(100):
	if num%F == 0:
		print(str(num)[-2:])
		break
	else:
		num += 1


# while True:
# 	if count >= 100:
# 		break
# 	if int(N)%F == 0:
# 		print('00')
# 		break
# 	if num%F == 0:
# 		print('%02d' %count)
# 		break
# 	else:
# 		num += 1
# 		count += 1


# 다른 사람 풀이1 왜 위에건 틀리고 아래는 안틀렸다고 나오지??
# n = input()
# f = int(input())
# a = int(n[:-2] + '00')
# while True:
#     if a % f == 0:
#         break
#     a += 1
# print(str(a)[-2:])
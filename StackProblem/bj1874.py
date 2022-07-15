# 스택 수열

n = int(input())

bucket = []
seq = []
bucket2 = []
state = []
for i in range(n):
    num = int(input())
    bucket.append(num)

nextNum = 0
for number in range(1, n+1):
    seq.append(number)
    state.append('+')

    while len(seq) > 0 and seq[-1] == bucket[nextNum]:
        seq.pop()
        bucket2.append(bucket[nextNum])
        state.append('-')
        nextNum += 1

if bucket == bucket2:
    for k in state:
        print(k)
else:
    print('NO')


# 다른 사람 풀이. 실시간으로 입력된 값을 비교하여 push와 pop을 진행하고
# pop의 도중 입력된 값과 일치하지 않으면 바로 NO를 출력한다.
import sys
n = int(sys.stdin.readline())
stk = []
make = []
cur = 1
chk = 0

for i in range(n):
	num = int(sys.stdin.readline())
	
	while cur <= num: # 이 while 부분의 아이디어가 좋은듯.
		stk.append(cur)
		make.append("+")
		cur += 1

	if stk[-1] == num:
		stk.pop()
		make.append("-")
	else:
		print("NO")
		chk = 1
		break

if chk == 0:
	for i in make:
		print(i)

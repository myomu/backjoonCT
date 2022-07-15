# 균형잡힌 세상
# 아래 조건식 반례 https://www.acmicpc.net/board/view/74929
# [([]]) << 이게 문제였음..;; 아래 if 문에서 check 못하는 부분.

# import sys

# n = ' '
# while n != '.':
#     n = input()#sys.stdin.readline().rstrip()
#     if n == '.': # 아래 주석에서 생긴 문제를 해결하기 위한 if문
#         break
#     li = []
#     answer = ''
#     cnt1 = cnt2 = 0
#     for i in n:
#         if i in '()[]':
#             li.append(i)
#         if i == '(':
#             cnt1 += 1
#         if i == ')':
#             cnt1 -= 1
#         if i == '[':
#             cnt2 += 1
#         if i == ']':
#             cnt2 -= 1

#         if cnt1 < 0 or cnt2 < 0:
#             answer = 'no'
#             break

#         if len(li) > 1:
#             if li[-2] == '(':
#                 if li[-1] == ']':
#                     answer = 'no'
#                     break
#             if li[-2] == '[':
#                 if li[-1] == ')':
#                     answer = 'no'
#                     break

#     if len(li)%2 != 0 or cnt1 != 0 or cnt2 != 0:
#         answer = 'no'
#     if answer != 'no':
#         answer = 'yes'
#     print(answer) # 첫 번째 틀린 이유.. 그냥 . 만 입력해서 종료시키면 yes를 출력하고 종료된다... ㅎㅎ;;


# 결국은 반례 회피 찾기 힘들어서 다른 풀이 참고하여 풀게되었음. stack을 이용해서 더 짧고 간결하게 풀던 것을 발견..
# 이것도 틀리긴 했는데 반례를 찾음. https://www.acmicpc.net/board/view/76389 [()][.
while True:
    n = input()
    stack = []
    ans = ''
    if n == '.':
        break
    for i in n:
        if i in '([':
            stack.append(i)
        elif i == ')':
            if not stack or stack[-1] == '[':
                ans = 'no'
                break
            elif stack[-1] == '(':
                ans = 'yes'
                stack.pop()
        elif i == ']':
            if not stack or stack[-1] == '(':
                ans = 'no'
                break
            elif stack[-1] == '[':
                ans = 'yes'
                stack.pop()
    if not stack and ans != 'no': # 위의 반례를 반영. stack이 비어있지 않으면 ans는 no이다.
        ans = 'yes'
    else:
        ans = 'no'
    print(ans)


# 아래는 다른 사람풀이. 코드를 더울 줄였다고 보면 된다. 원리는 비슷.
import sys
def solution2(s):
	l = []
	for c in s:
		if c in '([':
			l.append(c)
		if c == ')':
			if not l or l.pop() != '(':
				return "no"
		if c == ']':
			if not l or l.pop() != '[':
				return "no"
	if l:
		return "no"
	return "yes"

if __name__ == "__main__":
	l = sys.stdin.readlines()
	l.pop()

	for s in l:
		print(solution2(s))

        
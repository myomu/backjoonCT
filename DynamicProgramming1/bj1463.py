# 1로 만들기

# 전략
# 처음부터 3으로 나눠지면 3으로 나눈다. 그러나 나뉘지 않으면 다음 단계.
# 1을 빼서 3으로 나눠지면 그것이 best. 안되면 2로 나눈다.
# 위 전략은 fail..

# 아래는 질문글에서 어떤 유저의 말씀
''' 그리고 이 코드는 dp라고 부르기 어렵습니다.
현재 N을 보고 최적이 되는 다음 N을 직접 골라 그 방향으로만 나아가기 때문입니다.
dp가 되려면 모든 가능성을 열어두고 다 해본 뒤 그 중 최적을 고르는 형식이 되어야 합니다.
3으로 나누어 떨어진다고 해서 바로 3으로 나누는 게 최적이라는 보장도 없고,
1을 뺀 뒤 3으로 나눌 수 있다고 해서 그렇게 하는 게 최적이라는 보장도 없고,
2로 나누어 떨어진다고 해서 2로 바로 나누는 게 최적이라는 보장도 없습니다.
그저 추측에 불과합니다.
'''

# 시간 640ms
X = int(input())
d = [0 for _ in range(X+1)]

for i in range(2, X+1):
    d[i] = d[i-1] + 1 # 아래 3혹은 2로 나누어지지 않는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1) # 1을 빼는 경우와 3으로 나눌 경우 비교
        # +1은 3으로 나눌 때 1번 count 하는 것을 체크
    if i % 2 == 0: ## 여기를 elif 로 하면 3으로 나누는 경우 이 조건을 실행하지 않는다. 그래서 틀렸다고 나온다.
        # 그 이유인 즉 2혹은 3으로 나누어지는 숫자의 경우 3으로 나누는 것과 2로 나누는 것
        # 어느 것이 더 적은지 비교하지 않기 때문이다.
        d[i] = min(d[i], d[i//2] + 1) # 1을 빼는 것과 2로 나눌 경우 비교

print(d[X])

#Case 2 - 시간: 80ms
def make_one(n,lst):
    if n==1:
        return 0
    elif lst[n] != -1:  #저장되어 있다면 불러오기
        return lst[n]
    else:               #저장안되어 있다면 저장하기
        if n % 6 == 0: 
            lst[n] = min(make_one(n//3,lst), make_one(n//2,lst)) +1
        elif n %3 == 0: 
            lst[n] = min(make_one(n//3,lst), make_one(n-1,lst)) +1
        elif n %2 == 0: 
            lst[n] = min(make_one(n//2,lst), make_one(n-1,lst)) +1
        else: 
            lst[n] = make_one(n-1,lst) +1
        return lst[n]


n = int(input())
case = [-1] * (n+1)         #DP에 사용할 리스트 생성
case[0],case[1] = False,0

print(make_one(n,case))

# 페기
# cnt = 0
# while X > 1:
#     print(f'X = {X}, cnt = {cnt}')
#     if X % 3 == 0:
#         X //= 3
#     elif (X-1) % 3 == 0:
#         X -= 1
#         X //= 3
#         cnt += 1
#     elif X % 2 == 0:
#         X //= 2
#     else:
#         X -= 1
#     cnt += 1
        
# print(cnt)
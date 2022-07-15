# 영화감독 숌
# 브루트 포스 방식.. 모든 경우의 수를 탐색. 그냥 1씩 증가시켜서 666이 포함된 것을 카운팅 하는 방식이다.

n = int(input())

titleNumber = 666
result = 0
while n:
    if '666' in str(titleNumber):
        titleNumber += 1
        n -= 1
    else:
        titleNumber += 1
print(titleNumber-1)
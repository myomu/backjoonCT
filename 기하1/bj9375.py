# 패션왕 신해빈
# https://www.acmicpc.net/board/view/43867
# TypeError: unhashable type: 'list'
# 위 에러 해결법 위에 링크. 즉, set을 사용할 때 리스트 안에 요소들은 변경 불가능한 값들이어야한다.
# 이중 리스트를 넣었을 때 위 에러가 뜬다..(문자열, 숫자, 튜플 만)

import sys

T = int(input())

for _ in range(T):
    li = []
    d = dict()
    N = int(input())

    for _ in range(N):
        clothes, clothes_type = sys.stdin.readline().rstrip().split()       
        if d.get(clothes_type, 0):
            d[clothes_type].append(clothes)
        else:
            d[clothes_type] = [clothes]

    cnt = 1
    for i in d:
        cnt *= (len(d[i])+1) #의상을 벗는 경우가 있기 때문에 1을 더해준다.
    print(cnt-1) #각각의 의상 종류를 전부 벗는 경우가 1개 존재함으로 1을 빼준다.
# Strfry

N = int(input())
for _ in range(N):
    string, target = input().split()
    li1, li2 = [0 for _ in range(26)], [0 for _ in range(26)]
    for i in string:
        loc = ord(i)-97
        li1[loc] += 1
    for j in target:
        locs = ord(j)-97
        li2[locs] += 1
    if li1 == li2:
        print('Possible')
    else:
        print('Impossible')


## 다른 사람 풀이1
# 초 간단..ㅋㅋㅋ 그냥 둘다 정렬해서 비교하면 끝. 하나씩 리스트 값 올려줄 필요없더라..

def solution(T):
    a, b = map(lambda x : sorted(list(x)), input().split())
    print(a == b and "Possible" or "Impossible")

for T in range(1, int(input()) + 1):
    solution(T)


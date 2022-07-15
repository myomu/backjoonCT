# 인간-컴퓨터 상호작용
# 처음은 문자열크기의 리스트를 26개 만든 다음 문자열의 문자를 하나씩 받아 해당 문자에 해당하는 리스트에 문자열의 위치를
# +1 하는 방식을 사용했다. 원하는 문자에 해당하는 리스트를 찾아 그 범위만큼만을 sum 하게 되면 입력된 범위의
# 문자의 개수 합을 구할 수 있다.
# 그러나 이 방식은 누적합을 통해 풀기 어려워 20만*20만의 상황에서 시간초과가 발생하는 모양이다.

# 그래서 다시 방법을 찾아보았고 이중 리스트의 구성을 반대로 26개의 리스트를 문자열의 수만큼 생성한다.
# 들어오는 문자 하나가 a 라면 li[0][ord('a')-97]의 위치에 1을 넣어주고
# 다음에도 a가 들어오면 li[1][ord('a')-97] = li[0][ord('a')-97] + 1을 해주는 것이다.
# 이렇게 누적시켜서 최대범위 값 - 최소범위 값으로 빼면 원하는 범위의 문자 개수가 도출될 것이다.
 
# import sys

# input = sys.stdin.readline
# S = input().rstrip()
# q = int(input())
# li = [[0]*len(S) for _ in range(26)]

# for i in range(len(S)):
#     s = ord(S[i]) - 97
#     li[s][i] += 1
#     for j in range(26):
#         li[j][i] += li[j][i-1]

# print(li)
# for _ in range(q):
#     a, l, r = input().split()
#     l, r = map(int, [l, r])
#     ans = sum(li[ord(a)-97][r+1])
#     sys.stdout.write(str(ans)+'\n')

import sys

input = sys.stdin.readline
S = input().rstrip() # strip()을 취하지 않으면 문자열의 경우 \n가 존재해서 총 길이가 +1 된다.
q = int(input())
li = [[0]*26 for _ in range(len(S))]

li[0][ord(S[0])-97] = 1
for i in range(1, len(S)):
    s = ord(S[i]) - 97
    li[i][s] = 1
    for j in range(26):
        li[i][j] += li[i-1][j] # i-1이므로 시작을 1부터 시작한다.

for _ in range(q):
    a, l, r = input().split()
    a = ord(a) - 97
    l, r = map(int, [l, r])
    if l > 0:
        ans = li[r][a] - li[l-1][a] # l-1 과 l > 0 조건의 이유는 l이 0일때를 대비하기 위함이다.
    else:
        ans = li[r][a]
    sys.stdout.write(str(ans)+'\n')


'''
# 다른 사람 풀이
import sys
input = sys.stdin.readline

s = input().rstrip()
n = int(input())

cnt = [[0]*26 for _ in range(len(s)+1)]


for i in range(1,len(s)+1):
    cnt[i] = cnt[i-1].copy() # 요 부분이 가장 큰 차이점인듯?!
    cnt[i][ord(s[i-1])-97] += 1

for i in range(n):
    a,l,r = input().split()
    num = ord(a)-97
    count =  cnt[int(r)+1][num] - cnt[int(l)][num]
    print(count)
'''
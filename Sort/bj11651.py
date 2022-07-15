# 좌표 정렬하기 2 sorted의 lambda를 사용 2번째 값을 우선 정렬 1번째 값은 그 다음 우선순위로 오름차순 정렬한다.
# import sys sys.stdin.readline() 사용하면 시간 더 줄어들듯?

n = int(input())
bucket = []
for _ in range(n):
    x, y = map(int, input().split())
    bucket.append([x, y])

bucket = sorted(bucket, key = lambda x : (x[1], x[0]))

for i in bucket:
   print(i[0], i[1])

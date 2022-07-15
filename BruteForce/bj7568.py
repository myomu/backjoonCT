# 덩치

N = int(input())

people = []

for i in range(N):
    weight, height = map(int, input().split())
    people.append([weight, height, 1])

print(people)

for j in range(N):
    if j+1 == N:
        break
    for k in range(j+1, N):
        # if people[j][0] == people[k][0] and people[j][1] == people[k][1]:

        if people[j][0] < people[k][0] and people[j][1] < people[k][1]:
            people[j][2] += 1
        elif people[j][0] > people[k][0] and people[j][1] > people[k][1]:
            people[k][2] += 1
        else:
            continue

print(people)
for rank in people:
    print(rank[2], end =' ')


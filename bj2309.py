# 일곱 난쟁이

# dwarf = []
# seven = []
# for i in range(9):
#     dwarf.append(int(input()))

# def findDwarf(num):
#     if len(seven) == 7 and sum(seven) == 100:
#         seven.sort()
#         print(seven)
#         #print(*seven, sep='\n')
#         #exit(0)
#     else:
#         for i in range(9):
#             if i != num:
#                 seven.append(dwarf[i])
#                 findDwarf(num)
#                 seven.pop()

# findDwarf(-1)


# 위에 내가 푼건 재귀로 불었고 모든 구간을 탐색하다가 exit로 탈출하는 방식.
# 그런데 depth를 쓸 이유가 있나?? 오류가 있고 중복된 값을 집어넣는 경향이 있어 엄연히 따지자면 틀리지 않았나 싶다.
# 아니 다시 생각해보니.. 처음 하나를 찾을 땐 중복이 안되나 본데? ;; 
# depth를 빼버리니까 maximum recursion depth exceeded in comparison 오류가 뜬다. 재귀 한도에 걸림.

# 아래가 시간이 더 적게 걸리더라. 명확한 해답이기도하다.
# heights = []

# tmp1, tmp2 = 0,0

# for _ in range(9):
#     heights.append(int(input()))

# # 총 9명 중 2명을 제하여 합이 100이 되는지 파악하는 방식.
# for i in range(9):
#     for j in range(i+1, 9):
#         if sum(heights) - (heights[i]+heights[j]) == 100: # 이 부분의 아이디어가 좋았음.
#             tmp1, tmp2 = heights[i], heights[j]

# heights.remove(tmp1)
# heights.remove(tmp2)

# heights.sort()

# for n in range(7):
#     print(heights[n])



dwarf = []
d1 = d2 = 0

for _ in range(9):
    dwarf.append(int(input()))

for i in range(9):
    for j in range(i+1, 9):
        if sum(dwarf) - (dwarf[i] + dwarf[j]) == 100:
            d1 = dwarf[i]
            d2 = dwarf[j]
            
dwarf.remove(d1)
dwarf.remove(d2)
dwarf.sort()
print(*dwarf, sep='\n')
# 직각삼각형

while True:
    li = list(map(int, input().split()))
    li.sort()
    c1, c2, h = li[0], li[1], li[2]
    if c1 == 0 and c2 == 0 and h == 0:
        break
    if c1 == 0 or c2 == 0 or h == 0:
        print('wrong')
        continue
    if ((c1**2) + (c2**2)) == h**2:
        print('right')
    else:
        print('wrong')
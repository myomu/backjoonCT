# 네 번째 점

width = []
height = []
a, b = 0, 0

for _ in range(3):
    w, h = map(int, input().split())
    width.append(w)
    height.append(h)

if width.count(min(width)) == 1:
    a = min(width)
else:
    a = max(width)

if height.count(min(height)) == 1:
    b = min(height)
else:
    b = max(height)

print(a, b)
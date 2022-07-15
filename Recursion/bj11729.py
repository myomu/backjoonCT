# 하노이 탑 이동 순서
# 재귀 이용?? 하노이탑 공식을 참고

def printMoving(diskNum, startRod, endRod):
    #print(f'{diskNum}번 원판을 {startRod}에서 {endRod}로 이동')
    print(startRod, endRod)

def hanoi(lastDisk, startRod, endRod):
    #print(lastDisk, startRod, endRod)
    if lastDisk == 0:
        return

    otherRod = 6 - (startRod + endRod) # 요게 핵심 포인트 인듯?
    hanoi(lastDisk-1, startRod, otherRod)
    printMoving(lastDisk, startRod, endRod)
    hanoi(lastDisk-1, otherRod, endRod)



n = int(input())
print(2**n-1)
hanoi(n, 1, 3)
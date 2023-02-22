import math
h = int(input())
m = int(input())
time = h * 60 + m + 15
calcH = math.floor(time / 60)
calcM = time % 60
if calcH > 23:
    calcH = 0

if calcM < 10:
    print(f'{calcH}:0{calcM}')
else:
    print(f'{calcH}:{calcM}')

import sys

n = int(input())
routes = list(sys.stdin.readline().split())

x = 1
x1 = 0
y = 1
y1 = 0

direction = ['L', 'R', 'U', 'D']
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for route in routes:
    for i in range(4):
        if direction[i] == route:
            x1 = x + dx[i]
            y1 = y + dy[i]

    if x1 < 1 or x1 > n or y1 < 1 or y1 > n:
        continue

    x, y = x1, y1

print(y, x)
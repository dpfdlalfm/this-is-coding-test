location = list(input())
x = ord(location[0])
y = int(location[1])

cnt=0
steps = [[-1,-2],[1,-2],[2,-1],[2,1],[-1,2],[1,2],[-2,1],[-2,-1]]

for step in steps:
    dx = x + step[0]
    dy = y + step[1]
    if dx < ord('a') or dx > ord('h') or dy < 1 or dy > 8:
        continue
    cnt += 1

print(cnt)
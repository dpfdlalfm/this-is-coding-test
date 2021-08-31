n = int(input())
coins = [500,100,50,10]
cnt = 0

for coin in coins:
    cnt += n // coin
    n = n % coin

print("거슬러줘야 할 동전의 개수:", cnt)
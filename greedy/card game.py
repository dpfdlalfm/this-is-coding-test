import sys

n,m = map(int,sys.stdin.readline().split())

cards = []
for _ in range(n):
    cards.append(list(map(int,sys.stdin.readline().split())))
print(cards)

# result = 1                                # 방법 1
# for card in cards:
#     if min(card) > result:
#         result = min(card)

result = max(min(card) for card in cards)   # 방법 2
print(result)
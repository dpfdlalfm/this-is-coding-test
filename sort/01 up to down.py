# 이것이 코딩테스트다
# Chapter 4. 정렬 알고리즘
# 1번 위에서 아래로

def num_restrict(num,a,b):
    if num < a or num > b:
        sys.exit()

import sys
n = int(input())
num_restrict(n,1,500)

arr=[]
for _ in range(n):
    y = int(input())
    num_restrict(y,1,100000)
    arr.append(y)

arr = sorted(arr,reverse = True)
print(arr)
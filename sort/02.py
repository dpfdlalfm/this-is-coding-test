# 이것이 코딩테스트다
# Chapter 4. 정렬 알고리즘
# 2번 성적이 낮은 순서로 학생 출력하기

import sys

def num_restrict(num,a,b):
    if num < a or num > b:
        sys.exit()

n = int(input())
num_restrict(n,1,100000)

arr=[]
for _ in range(n):
    a, b = input().split()
    arr.append([a,int(b)])

arr = sorted(arr, key = lambda x:x[1])

for i in range(len(arr)):
    print(arr[i][0], end=' ')
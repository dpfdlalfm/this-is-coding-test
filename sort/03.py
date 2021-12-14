# 이것이 코딩테스트다
# Chapter 4. 정렬 알고리즘
# 3번 두 배열의 원소 교체

import sys

def arr_restrict(arr):
    if max(arr) >= 10000000 or min(arr) <= 0:
        sys.exit()

def num_restrict(num,a,b):
    if num < a or num > b:
        sys.exit()

n, k = map(int,input().split())
num_restrict(n,1,100000)
num_restrict(k,0,n)
arr1 = sorted(list(map(int,input().split())))
arr2 = sorted(list(map(int,input().split())), reverse=True)
arr_restrict(arr1)
arr_restrict(arr2)

print(sum(arr2[0:k])+sum(arr1[k:]))
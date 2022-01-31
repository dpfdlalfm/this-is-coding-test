import sys

# 이것이 코딩테스트다
# Chapter 08. 다이나믹 프로그래밍
# 피보나치 수열

n = int(input())
arr = [0]*100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if arr[x] != 0:
        return arr[x]

    arr[x] = fibo(x-1) + fibo(x-2)
    return arr[x]

print(fibo(n))
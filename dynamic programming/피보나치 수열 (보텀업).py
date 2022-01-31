import sys

# 이것이 코딩테스트다
# Chapter 08. 다이나믹 프로그래밍
# 피보나치 수열 (개선)
# 보텀업 방식. 작은 문제 -> 큰 문제로 해결

n = int(input())
arr = [0]*100
# DP table

arr[1] = 1
arr[2] = 1

for i in range(3, n+1):
    arr[i] = arr[i-1] + arr[i-2]

print(arr[n])
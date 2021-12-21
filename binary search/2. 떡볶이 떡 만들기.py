# 이것이 코딩테스트다
# Chapter 7. 이진 탐색
# 2. 떡볶이 떡 만들기
# 시간제한 2초
import sys


# 수의 범위를 제한시켜주는 함수
def num_restrict(x,a,b):
    if x<a or x>b:
        sys.exit()


# 떡의 개수 n과 요청한 떡의 길이 m 입력
n, m = map(int,sys.stdin.readline().split())
num_restrict(n,1,1000000) # 1 <= n <= 1,000,000
num_restrict(m,1,2000000000)
# 부품의 각 고유번호를 띄어쓰기로 구분해서 입력받음.
ddeok_lst = list(map(int, sys.stdin.readline().split()))
start = 0
end = max(ddeok_lst) # 시간복잡도 최대 1,000,000

result = 0
while start <= end: # 시간복잡도 최대 log2(1,000,000) = 20
    total = 0
    mid = (start + end) // 2
    for x in ddeok_lst: # 시간복잡도 최대 1,000,000
        # 절단기 높이보다 떡 길이가 클 때만 더함.
        if x > mid:
            total += x - mid
    # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽부분 탐색)
    if total < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
    # H의 최대값을 구하므로 결과값이 요청길이보다 크거나 같아도 됨.
    else:
        result = mid
        start = mid + 1
# 시간복잡도 1,000,000 + 20*1,000,000 -> 약 2100만이므로 시간제한 만족.

# def function(lst,m):
#     for i in range(max(lst)-1,0,-1):
#         # 떡의 최대 개수 : O(1,000,000) + 떡의 최대크기 : O(1,000,000,000) 이므로
#         # 시간제한 못 맞춤. -> 다른 방안 고려
#         sum = 0
#         for j in lst:
#             if j < i:
#                 continue
#             else:
#                 sum += (j - i)
#         if sum >= m:
#             return i
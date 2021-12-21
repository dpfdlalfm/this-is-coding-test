# 이것이 코딩테스트다
# Chapter 7. 이진 탐색
# 1. 부품 찾기
import sys


def binary_search(arr,target,start,end):
    while start <= end:
        mid = (start + end) // 2
        if target == arr[mid]:
            return 'yes'
        elif target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return 'no'


# 수의 범위를 제한시켜주는 함수
def num_restrict(x,a,b):
    if x<a or x>b:
        sys.exit()


# 부품의 재고 개수 n 입력
n = int(input())
num_restrict(n,1,1000000) # 1 <= n <= 1,000,000
# 부품의 각 고유번호를 띄어쓰기로 구분해서 입력받음.
stocks = list(map(int,sys.stdin.readline().split()))
# 부품의 요청 개수 m 입력
m = int(input())
num_restrict(m,1,100000)
# 요청 부품의 고유번호를 띄어쓰기로 구분해서 입력.
requests = list(map(int,sys.stdin.readline().split()))
# 이진탐색을 하기 위해 각각의 리스트를 정렬.
stocks.sort()
requests.sort()

for request in requests:
    # 부품이 존재하면 yes, 부품이 존재하지 않으면 no를 출력.
    print(binary_search(stocks,request,0,len(stocks)-1), end=' ')
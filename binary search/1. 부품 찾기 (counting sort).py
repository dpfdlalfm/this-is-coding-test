# 이것이 코딩테스트다
# Chapter 7. 이진 탐색
# 1. 부품 찾기
# 계수정렬을 이용한 문제 풀이
import sys


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

# stocks 의 최대값 만큼 0을 가진 배열 초기화.
# cnt_lst = [0 for i in range(max(stocks)+1)]
# 위 방법은 max 값을 찾는데 더 큰 시간이 걸리므로
# n의 최대값+1 만큼으로 초기화시킨다.
cnt_lst = [0] * 1000001

for stock in stocks:
    # 부품의 고유번호를 인덱스로 갖는 값을 +1
    cnt_lst[stock] += 1
for request in requests:
    if cnt_lst[request] == 0:
        print('no', end=' ')
    else:
        print('yes',end=' ')
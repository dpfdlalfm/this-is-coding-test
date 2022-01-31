import sys

def num_restrict(n,a,b):
    if a <= n <= b: pass
    else: sys.exit()

# 이것이 코딩테스트다
# Chapter 08. 다이나믹 프로그래밍
# 1로 만들기
# 보텀업 방식. 작은 문제 -> 큰 문제로 해결

n = int(input())
num_restrict(n,1,30000)
d = [0] * 30001
#! 수정 d = [0] * 30000
# 0이 포함되기 때문에 d의 크기를 +1까지 해줘야됨.

for i in range(2,n+1):
    d[i] = [i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)


#! 수정 아래코드는 답은 맞지만 항상 4가지 변수를 inf로 선언해야하지만
# 수정된 코드는 나누어 떨어지지 않는 경우에는 비교를 안해도 되기때문에
# 메모리적 측면에서 더 효율적이다.

# for i in range(2,n+1):
#     temp1 = temp2 = temp3 = temp4 = float('inf')
#     if i % 5 == 0:
#         temp1 = d[i/5] + 1
#     if i % 3 == 0:
#         temp2 = d[i/3] + 1
#     if i % 2 == 0:
#         temp3 = d[i/2] + 1
#     if i - 1 >= 1:
#         temp4 = d[i-1] + 1
    
#     d[i] = min(temp1,temp2,temp3,temp4)

print(d[i])
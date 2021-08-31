import sys

n,m,k = map(int,sys.stdin.readline().split())
num_lst = list(map(int,sys.stdin.readline().split()))

num_lst.sort()

# for i in range(m):                    # 방법 1
#     if i % (k+1) != k:
#         sum += num_lst[n-1]
#     else:
#         sum += num_lst[n-2]

cnt = m // (k+1)                        # 방법 2
p = num_lst[n-1] * k + num_lst[n-2]
sum = p * cnt

cnt = m % (k+1)
sum += cnt * num_lst[n-1]

print(sum)
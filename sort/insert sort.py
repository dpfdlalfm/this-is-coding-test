# 이것이 코딩테스트다
# Chapter 4. 정렬 알고리즘
# 퀵 정렬

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1,len(arr)):
    x = arr[i]
    k = 0
    for j in range(i):
        if x > arr[j]:
            k += 1
        else:
            break
    del arr[i]
    arr.insert(k,x)

# 책 소스코드

# for i in range(1,len(arr)):
#     for j in range(i,0,-1): # 인덱스 i부터 1까지 감소시킨다.
#         if arr[j] < arr[j-1]:
#             arr[j], arr[j-1] = arr[j-1], arr[j]   # 뒤에서 앞으로 한칸씩 비교하며 스와핑.
#         else:
#             break

print(arr)

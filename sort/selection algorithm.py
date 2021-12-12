# 이것이 코딩테스트다
# Chapter 4. 정렬 알고리즘
# 선택 정렬
# 시간 복잡도 O(n^2)

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(arr)):
    x = arr[i]
    for j in range(i+1, len(arr)):
        if x > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
            x = arr[i]
print(arr)
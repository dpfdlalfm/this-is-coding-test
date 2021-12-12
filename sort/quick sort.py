# 이것이 코딩테스트다
# Chapter 4. 정렬 알고리즘
# 퀵 정렬
# 시간복잡도 O(nlogn)
# 이미 정렬 되어있는 경우에는 O(n^2)

import sys
sys.setrecursionlimit(10000)

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(arr, start, end):
    if start >= end: # 원소가 1개일때는 종료
        return
    pivot = start
    # 피벗을 arr[start]로 설정하지 않는 이유는
    # arr[pivot]과 arr[right] 스와핑을 해야 하기 때문에.
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and arr[left] <= arr[pivot]:
            # 왼쪽에서부터 피벗보다 큰 원소가 없으면 한칸 더
            # 왼쪽에서부터 피벗보다 큰 원소를 찾으면 stop
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            # 오른쪽에서부터 피벗보다 작은 원소가 없으면 한칸 더
            # 오른쪽에서부터 피벗보다 작은 원소를 찾으면 stop
            right -= 1
        if left > right: # 엇갈릴 때는 작은 데이터와 피벗을 교체
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            arr[left], arr[right] = arr[right], arr[left]
    # 분할 이후 왼쪽부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(arr, start, right-1)
    quick_sort(arr, right+1, end)

quick_sort(arr, 0, len(arr)-1)
print(arr)
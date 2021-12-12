# 이것이 코딩테스트다
# Chapter 4. 정렬 알고리즘
# 계수 정렬
# 모든 데이터가 양의 정수이면서 abs(Max-Min) < 1,000,000
# 경우에만 사용가능
# 시간복잡도 O(n+k)

arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1,4,8,0,5,2]

def counting_sort(arr):
    cnt_arr = [[0, i] for i in range(max(arr)+1)]
    for i in range(len(arr)):
        cnt_arr[arr[i]][0] += 1

    result = []
    for i in range(len(cnt_arr)):
        for j in range(cnt_arr[i][0]):
            result.append(cnt_arr[i][1])
    return result

print(counting_sort(arr))
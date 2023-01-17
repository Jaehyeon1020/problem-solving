# 재귀함수로 구현한 이분탐색
def binary_search_recursive(array, target, start, end):
    # 찾는 결과 없는경우
    if start > end:
        return -1

    mid = (start + end) // 2

    if array[mid] < target:
        return binary_search_recursive(array, target, mid + 1, end)
    elif array[mid] > target:
        return binary_search_recursive(array, target, start, mid - 1)
    else:
        return mid


# 반복문으로 구현한 이분탐색
def binary_search_iter(array, target, start, end):
    # 값 찾을 때까지 반복 (값 없으면 start가 end보다 커짐)
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    
    # while문에서 return 못함 == 값 못찾음 -> return -1
    return -1

array = [1, 3, 5, 9, 12, 34, 55]
target = 12

if binary_search_iter(array, target, 0, len(array) - 1) == -1:
    print("찾는 값 없음")
else:
    print("찾는 값의 인덱스는:", binary_search_iter(array, target, 0, len(array) - 1))
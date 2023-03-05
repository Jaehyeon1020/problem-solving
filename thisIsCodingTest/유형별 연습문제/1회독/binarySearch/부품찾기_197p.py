n = int(input())
having = list(map(int, input().split()))
having.sort() # 이진 탐색 하기 전 반드시 정렬 필요
m = int(input())
wanting = list(map(int, input().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return "yes"
        elif array[mid] > target:
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1
        
    return "no"

for item in wanting:
    print(binary_search(having, item, 0, n - 1), end=' ')
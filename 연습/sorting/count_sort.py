arr = [3, 5, 8, 1, 2, 0, 9, 1, 2]

def count_sort(arr):
    count = [0 for _ in range(max(arr) + 1)]

    for i in arr:
        count[i] += 1
    
    for i in range(len(count)):
        for _ in range(count[i]):
            print(i, end=' ')

count_sort(arr)
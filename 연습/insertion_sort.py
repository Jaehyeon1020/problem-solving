arr = [7, 6, 8, 0, 3, 2, 10]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break
    
    print(arr)

insertion_sort(arr)
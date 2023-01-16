arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    print(arr)

selection_sort(arr)
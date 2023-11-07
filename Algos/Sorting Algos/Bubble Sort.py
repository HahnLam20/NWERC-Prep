def bubble_sort(arr):
    for itm in arr:
        for idx in range(len(arr) - 1):
            if arr[idx] > arr[idx + 1]:
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]


def binary_search(arr, val):
    low = 0
    high = len(arr)

    while low < high:
        mid = low + (high - low) // 2

        if arr[mid] == val:
            return arr[mid]
        elif arr[mid] < val:
            low = mid + 1
        elif arr[mid] > val:
            high = mid

    return None

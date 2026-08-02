def binarySearch(arr, key):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1

    return -1

arr = [5, 8, 15, 20, 30, 56, 60]
key = 56

ans = binarySearch(arr, key)

if ans != -1:
    print("Element found at index:", ans)
else:
    print("Element not found")
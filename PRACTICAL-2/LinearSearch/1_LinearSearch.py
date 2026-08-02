def linearSearch(arr, n, key):
    for i in range(n):
        if arr[i] == key:
            return i
    return -1

arr = [12, 78, 90, 23, 67, 54]
n = len(arr)
key = 23

ans = linearSearch(arr, n, key)

if ans != -1:
    print("Element found at index:", ans)
else:
    print("Element not found")
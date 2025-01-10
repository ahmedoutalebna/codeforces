def replace_elements(arr):
    n = len(arr)
    max_right = -1
    if n == 0:
        return []
    for i in range(n-1, -1, -1):
        current = arr[i]
        arr[i] = max_right
        max_right = max(arr[i], current)
    return arr

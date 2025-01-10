def majority(arr):
    count = 0
    for num in arr:
        if arr.count(num) > (len(arr) / 2):
            var = arr.count(num)
            if var > count:
                count = num
    return count

print(majority([3, 2, 3]))

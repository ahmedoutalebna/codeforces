def maxProductDifference(nums):
    arr = sorted(nums)
    a, b, c, d = arr[0], arr[1], arr[-1], arr[-2]
    return (c * d) - (a * b)

print(maxProductDifference([4,2,5,9,7,4,8]))
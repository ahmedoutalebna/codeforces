def findErrosNums(nums):
    output = [0, 0]
    for i in range(1, len(nums) + 1):
        if nums.count(i) > 1:
            output[0] = i
        if i not in nums:
            output[1] = i
    return output
print(findErrosNums([1,2,2,4]))
def removeElements(nums, val):
    count = 0
    output = [k for k in nums]
    for index, char in enumerate(output):
        if char == val:
            nums[index] = "_"
        else:
            count += 1
    print(count, nums)

removeElements([3,2,2,3], 3)
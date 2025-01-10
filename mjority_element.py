def majorityElement(nums):
    output = []
    for i in range(len(nums)):
        if nums[i] not in output and nums.count(nums[i]) > len(nums) // 3:
            output.append(nums[i])
    return output

print(majorityElement([1, 2]))
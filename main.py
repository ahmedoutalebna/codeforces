def containsNearbyDuplicate(nums, k):
    # Example1:
    # Input: nums = [1, 2, 3, 1], k = 3
    # nums[3] = nums[0] and abs(3-0) <= 3
    # return true
    # Output: true
    # if len(nums) == len(set(nums)):
    #     return False
    window = {}
    # window = {4: 0, 1: 1, 2: 2, 3: 3, 1: 4, 5: 5}
    #
    for i in range(len(nums)):
        current = nums[i]
        if current in window and abs(i - window[current]):
            return True
        window[current] = i
    return False

print(containsNearbyDuplicate([4,1,2,3,1,5], 3))


def nextGreater(nums1, nums2):
    output = []
    for num1 in nums1:
        if nums2.index(num1) == len(nums2) - 1:
            output.append(-1)
        else:
            # getting the index of the current item in nums2
            idx = nums2.index(num1)
            subList = nums2[idx:]
            k = len(output)
            for item in subList:
                if item > num1:
                    output.append(item)
                    break
            if len(output) == k:
                output.append(-1)
    return output




print(nextGreater([4,1,2], [1,3,4,2]))
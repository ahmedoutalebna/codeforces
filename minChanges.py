def minOperations(s):
    # we will try to resolve this problem using
    # the next value technique
    # we will check each time if the next value if
    # it's equal to the prev one so in
    zeros_alternating = "0"
    ones_alternating = "1"
    for i in range(1, len(s)):
        if zeros_alternating[i-1] == "0":
            zeros_alternating += "1"
        if ones_alternating[i-1] == "0":
            ones_alternating += "1"
        if zeros_alternating[i-1] == "1":
            zeros_alternating += "0"
        if ones_alternating[i-1] == "1":
            ones_alternating += "0"

    zeros_counter = 0
    ones_counter = 0
    for k in range(len(s)):
        if s[k] != zeros_alternating[k]:
            zeros_counter += 1
        if s[k] != ones_alternating[k]:
            ones_counter += 1
    return min(zeros_counter, ones_counter)
print(minOperations("10010100"))
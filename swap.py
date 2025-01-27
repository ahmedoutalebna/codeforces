def minSwaps(s):
    counter = 0
    for idx, char in s:
        if idx + 1 < len(s):
            if char == s[idx + 1]:
                counter += 1
    return len(s) - counter - 1

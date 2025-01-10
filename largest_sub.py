from collections import Counter
def maxLengthBetweenEqualCharacters(s):

    if len(set(s)) == len(s): return -1
    arr1 = [[s[k], k] for k in range(len(s)) if s.count(s[k]) > 1]
    arr2 = [s[k] for k in range(len(s)) if s.count(s[k]) > 1]
    return arr2, arr1 

print(maxLengthBetweenEqualCharacters("scayofdzca"))
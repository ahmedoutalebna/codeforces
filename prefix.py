def longestCommonPrefix(strs):
    v = sorted(strs)
    first, last = v[0], v[-1]
    output = ""
    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return output
        output += first[i]
    return output

print(longestCommonPrefix(["abab","aba","abc"]))
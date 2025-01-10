def isIsomorphic(s, t):
    d = {}
    for idx, char in enumerate(s):
        if char in d:
            val = d[char]
            d[char] = t[idx]
            if d[char] != val:
                return False
        d[char] = t[idx]
    return len(set(d.keys())) == len(set(d.values()))


print(isIsomorphic('badc', 'baba'))

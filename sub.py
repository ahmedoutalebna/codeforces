def isSubsequence(s, t):

    sp = tp = 0
    while sp < len(s) and tp < len(t):
        if s[sp] == t[tp]:
            sp += 1
        tp += 1
    return sp == len(s)
#  Technique to solve this problem is to create a var named current_index
#  checks if the char at index is in s if it is then assign the index to the
#  current index and
#
print(isSubsequence("ab", "baab"))

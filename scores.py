def maxScore(s):
    scores = []
    for i in range(1, len(s)):
        zeros = s[:i].count("0")
        ones = s[i:].count("1")
        sc = zeros + ones
        scores.append(sc)
    return max(scores)


print(maxScore("011101"))
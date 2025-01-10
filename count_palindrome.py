def countPalindromicSubsequence(s):
    # set_pal = set()
    # # so the logic to solve this problem is to
    # for i in range(len(s)):
    #     first = s[i]
    #     for j in range(i+1, len(s)):
    #         second = s[j]
    #         for k in range(j+1, len(s)):
    #             third = s[k]
    #             if k < len(s):
    #                 pal = first + second + third
    #                 if pal == pal[::-1]:
    #                     set_pal.add(pal)
    # return len(set_pal)
    letters = set(s)
    ans = 0

    for letter in letters:
        i, j = s.index(letter), s.rindex(letter)
        between = set()

        for k in range(i + 1, j):
            between.add(s[k])

        ans += len(between)

    return ans
print(countPalindromicSubsequence("aabca"))

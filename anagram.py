def groupAnagram(anagram):
    anagrams = []
    for k in range(len(anagram)):
        for i in range(len(anagram)):
            if k != i:
                if sorted(anagram[k]) == sorted(anagram[i]):
                    pass
print(groupAnagram(["act","pots","tops","cat","stop","hat"]))
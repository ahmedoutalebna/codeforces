def wordPattern(pattern, s):
    words = s.split(" ")
    charToWord = {}
    wordToChar = {}
    for c, w in zip(pattern, words):
        if c in charToWord and charToWord[c] != w:
            return False
        if w in wordToChar and wordToChar[w] != c:
            return False
        charToWord[c] = w
        wordToChar[w] = c
    return True

print(wordPattern("aaaa", "dog cat cat dog"))


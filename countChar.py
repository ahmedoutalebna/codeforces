from collections import Counter
def countChar(words, char):
    ch = Counter(char)
    result = 0
    for word in words:
        checked = False
        count = 0
        for w in word:
            if ch[w] < word.count(w):
                checked = True
                break
            count += 1
        if not checked:
            result += count
    return result



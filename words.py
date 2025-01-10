from collections import Counter
def countCharacters(words, chars):
    chars_collection = Counter(chars)
    total = 0
    for word in words:
        hashing = Counter(word)
        can_form = True
        for w in word:
            if hashing[w] > chars_collection.get(w, 0):
                can_form = False
                break
        if can_form:
            total += len(word)
    return total


print(countCharacters(["hello","world","leetcode"], "welldonehoneyr"))
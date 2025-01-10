from collections import Counter
def makeEqual(words):
    recycle = "".join(words)
    d = Counter(recycle)
    for v in d.values():
        if v % len(words) != 0:
            return False
    return True

print(makeEqual(["abc","aabc","bc"]))
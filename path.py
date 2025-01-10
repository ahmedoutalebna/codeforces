from collections import Counter
def isPathCrossing(path):
    x = 0
    y = 0
    cross = [(0, 0)]
    for p in path:
        if p == "N":
            y += 1
        if p == "E":
            x += 1
        if p == "S":
            y -= 1
        if p == "W":
            x -= 1
        if (x, y) in cross:
            return True
        cross.append((x, y))

    return False



print(isPathCrossing('NES'))
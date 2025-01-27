def interchangeableRectangles(rectangles):

    res = 0
    for i in range(1, len(rectangles)):
        for j in range(i):
            if rectangles[i][0] / rectangles[i][1] == rectangles[j][0] / rectangles[j][1]:
                res += 1
    return res
print(interchangeableRectangles([[4,5],[7,8]]))
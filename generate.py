def generate(numRows):
    pascal = [[1]]
    if numRows == 1: return pascal
    if numRows == 2:
        pascal.append([1, 1])
    if numRows > 2:
        pascal = [[1], [1,1]]
        for i in range(2, numRows):
            item = [1]
            for k in range(1, len(pascal[i-1])):
                newItem = pascal[i-1][k] + pascal[i-1][k-1]
                item.append(newItem)
            item.append(1)
            pascal.append(item)
    return pascal






print(generate(2))
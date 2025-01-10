def largestGoodInteger(num):
    output = set()
    for k in num:
        if num.count(k) >= 3:
            output.add(k)
    final = []
    for s in output:
        nm = s*3
        if nm in num:
            final.append(int(nm))
    return final
print(largestGoodInteger("4818042931906802860005960222213336669500011846936171709111"))


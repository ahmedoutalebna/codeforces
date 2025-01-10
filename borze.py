borze = [it for it in input()]
decode = ""

for k, item in enumerate(borze):
    if (item == "." and k == 0) or (item == "." and k != 0 and borze[k-1] != "-"):
        decode += "0"
    if k+1 < len(borze):
        if item == "-" and borze[k+1] == ".":
            decode += "1"
        if item == "-" and borze[k+1] == "-":
            decode += "2"
print(decode)
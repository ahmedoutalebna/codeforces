def encode(strs):
    encoded = ""
    for s in strs:
        encoded += f"{len(s)}#" + s
    return encoded

    # 4#neet4#code4#love3#you


def decode(str):
    decoded = []
    for k, s in enumerate(str):
        

print(encode(['neet', 'code', 'love', 'you']))
print(decode("neet#code#love#you"))

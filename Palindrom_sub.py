def palindrom_sub(s):
    output = set()
    for i in range(len(s)):
        first = s[i]
        second = s[i+1]
        pal = first + second
        if i + 2 <= len(s) - 1:
            pal += s[i+2]
            if pal == pal[::-1]: output.add(pal)
            

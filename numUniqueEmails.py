def numUniqueEmails(emails):
    uniqueMails = set()
    for email in emails:
        e = email.split('@')
        if len(e) == 2:
            first = ''
            for char in e[0]:
                if char == '.':
                    pass
                elif char == "+":
                    break
                else:
                    first += char
            mail = first + '@' + e[1]
            uniqueMails.add(mail)
    return len(uniqueMails)

print(numUniqueEmails(["test.email+alex@leetcode.com","test.email.leet+alex@code.com"]))

def timeRequiredToBuy(tickets, k):
    seconds = 0
    # for ticket in tickets:
    #     if ticket <= tickets[k]:
    #         seconds += ticket
    #     if ticket > tickets[k]:
    #         seconds += tickets[k]
    # return seconds,
    seconds = 0
    iter = 0
    while tickets[k] > 0:
        if iter == len(tickets):
            iter = 0
        if tickets[iter] > 0:
            seconds += 1
            tickets[iter] -= 1
        iter += 1

    return seconds

print(timeRequiredToBuy([5,1,1,1], 0))

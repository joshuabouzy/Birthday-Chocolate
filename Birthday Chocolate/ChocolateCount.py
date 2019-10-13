def birthday(s, d, m):
    count = 0
    iteration = len(s) - (m - 1)
    for x in range (0, iteration):
        sub = s[x:x+m]
        if sum(sub) == d:
            count+=1
    return count

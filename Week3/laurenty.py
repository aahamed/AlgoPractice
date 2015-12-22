def laurenty(a, b):
    t = []
    for i in range(len(b)):
        sum1 = 0
        for j in range(len(a), i-1, -1):
            sum1 += a[2, j]
        sum2 = 0
        for j in range(0, i):
            sum2 += a[i, j]
        total = sum1 + sum2 + b[i]
        t.append(total)

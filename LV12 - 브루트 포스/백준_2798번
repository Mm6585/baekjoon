n, m = map(int, input().split())
l = list(map(int, input().split()))

dif = 300000
for i in range(len(l)):
    for j in range(len(l)):
        if (i == j):
            continue
        for k in range(len(l)):
            if ((i == k) or (j == k)):
                continue
            if (m - (l[i] + l[j] + l[k]) == 0):
                s = l[i] + l[j] + l[k]
                break
            elif (0 < (m - (l[i] + l[j] + l[k])) < dif):
                s = l[i] + l[j] + l[k]
                dif = m - s
                
print(s)

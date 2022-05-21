x, y = map(int, input().split())
a = []
for _ in range(x):
    a.append(input())

min = 99999

for j in range(y-7):
    for i in range(x-7):
        b = []
        for k in range(i, i+8):
            b.append(a[k][j:j+8])
        
        c = b.copy()
        if (b[0][0] == 'W'):
            s = 'B'
            for k in range(1, 8):
                s = s + b[0][k]
            c[0] = s
        else:
            s = 'W'
            for k in range(1, 8):
                s = s + b[0][k]
            c[0] = s
        b += c

        for m in range(2):
            cnt = m
            for n in range(8*m, 8*(m+1)):
                if ((n != 8*m) and (b[n-1][0] == b[n][0])):
                    cnt += 1
                    if (b[n][0] == 'W'):
                        s = 'B'
                        for k in range(1, 8):
                            s = s + b[n][k]
                        b[n] = s
                    else:
                        s = 'W'
                        for k in range(1, 8):
                            s = s + b[n][k]
                        b[n] = s
                for l in range(1, 8):
                    if (b[n][l-1] == b[n][l]):
                        cnt += 1
                        s = ''
                        if (b[n][l] == 'W'):
                            for k in range(l):
                                s = s + b[n][k]
                            s = s + 'B'
                            for k in range(l+1, 8):
                                s = s + b[n][k]
                            b[n] = s
                        else:
                            for k in range(l):
                                s = s + b[n][k]
                            s = s + 'W'
                            for k in range(l+1, 8):
                                s = s + b[n][k]
                            b[n] = s
            if (cnt < min):
                min = cnt

print(min)

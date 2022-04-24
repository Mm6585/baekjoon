t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    a = n % h
    if (a == 0):
        a = h
        b = n // h
    else:
        b = n // h + 1
    print(a*100 + b)

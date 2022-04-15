a, b, c = map(int, input().split())

if (a == b):
    if (b == c):
        price = 10000 + a*1000
    else:
        price = 1000 + a*100
else:
    if ((b==c) or (a==c)):
        price = 1000 + c*100
    else:
        price = max(a, b, c)*100
        
print(price)

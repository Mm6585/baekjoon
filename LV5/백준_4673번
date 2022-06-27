def d(n):
    a = str(n)
    sum = 0
    for i in range(len(a)):
        sum += int(a[i])
    sum += n
    
    return sum

array = []
for i in range(10000):
    array.append(d(i+1))
    
for i in range(10000):
    if (array.count(i+1) == 0):
        print(i+1)

def f(x):
    x = str(x)
    a = []
    for i in range(len(x)-1):
        a.append(int(x[i+1]) - int(x[i]))
    a = set(a)
    if (len(a) > 1):
        return 0
    else:
        return 1

n = int(input())
cnt = 0
for i in range(n):
    cnt += f(i+1)
print(cnt)

# 1 << better
l = []
n = int(input())

for _ in range(n):
    l.append(int(input()))

l.sort()
for i in l:
    print(i)

# 2
l = []
n = int(input())

for _ in range(n):
    l.append(int(input()))

for i in range(n):
    for j in range(n):
        if (i == j):
            continue
        if (l[i] > l[j]):
            tmp = l[i]
            l[i] = l[j]
            l[j] = tmp
    
for i in l:
    print(i)

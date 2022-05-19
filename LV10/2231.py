n = int(input())
m = '0'

for i in range(1, n):
    s = str(i)
    for j in s:
        i += int(j)
    if (n == i):
        m = s
        break

print(m)

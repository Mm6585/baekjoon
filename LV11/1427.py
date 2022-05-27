n = input()
l = [0] * 10
s = ''

for i in range(len(n)):
    l[int(n[i])] += 1

for i in range(len(l)-1, -1, -1):
    for _ in range(l[i]):
        s += str(i)

print(s)

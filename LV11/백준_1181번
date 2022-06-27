import sys
input = sys.stdin.readline

n = int(input())
l = []
m = []

for _ in range(n):
    s = input().rstrip()
    if (l.count(s) == 0):
        l.append(s)
        m.append(len(s))

l = list(zip(l, m))
l.sort(key=lambda x : (x[1], x[0]))

for i in l:
    print(i[0])

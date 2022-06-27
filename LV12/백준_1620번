import sys
input = sys.stdin.readline
 
n, m = map(int, input().split())
l = {}
r = [''] * m
 
for i in range(n):
    l[i] = input().rstrip()
 
f = dict(map(reversed, l.items()))
 
for i in range(m):
    s = input().rstrip()
    if (s.isdigit()):
        r[i] = l.get(int(s)-1)
    else:
        r[i] = int(f.get(s)) + 1
 
for i in r:
    print(i)

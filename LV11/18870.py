import sys
input = sys.stdin.readline
 
n = int(input())
l = list(map(int, input().split()))
 
s = sorted(set(l))
d = {x:y for y, x in enumerate(s)}
r = [d[i] for i in l]
 
for i in r:
	print(i, end=' ')

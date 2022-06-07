import sys
input = sys.stdin.readline
 
n, m = map(int, input().split())
dic = {}
 
for i in range(n):
    dic[i] = input().rstrip()
dic_r = dict(map(reversed, dic.items()))
 
l = []
for _ in range(m):
	s = input().rstrip()
	if (s in dic_r):
		l.append(s)
 
l.sort()
print(len(l))
for i in l:
    print(i)

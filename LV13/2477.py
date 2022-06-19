import sys
input = sys.stdin.readline

l = list()
li = list()
n = int(input())

for i in range(6):
    k, v = map(int, input().split())
    li.append([i, v])
    l.append([v, i])
l.sort()

p_idx = l[5][1]-1
if (p_idx == -1):
	p_idx = 5
n_idx = l[5][1]+1
if (n_idx == 6):
	n_idx = 0
if (li[p_idx][1] > li[n_idx][1]):
	s_idx = li[p_idx][0]
	a = li[p_idx][1] - li[n_idx][1]
else:
	s_idx = li[n_idx][0]
	a = li[n_idx][1] - li[p_idx][1]

p_idx = s_idx-1
if (p_idx == -1):
	p_idx = 5
n_idx = s_idx+1
if (n_idx == 6):
	n_idx = 0
if (li[p_idx][1] > li[n_idx][1]):
	b = li[p_idx][1] - li[n_idx][1]
else:
	b = li[n_idx][1] - li[p_idx][1]

print((l[5][0]*li[s_idx][1] - a*b) * n)

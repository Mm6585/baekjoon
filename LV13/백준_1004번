import sys
input = sys.stdin.readline
 
t = int(input())
 
for _ in range(t):
	startx, starty, endx, endy = map(int, input().split())
	n = int(input())
	cnt = 0
 
	for _ in range(n):
		x, y, r = map(int, input().split())
		sd = ((startx-x)**2 + (starty-y)**2)**(1/2)
		ed = ((endx-x)**2 + (endy-y)**2)**(1/2)
 
		if ((sd < r and ed > r) or (sd > r and ed< r)):
			cnt += 1
 
	print(cnt)

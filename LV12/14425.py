import sys
input = sys.stdin.readline
 
n, m = map(int, input().split())
l = [input() for _ in range(n)]

cnt = 0
for _ in range(m):
    s = input()
    if (s in l):
        cnt += 1
    
print(cnt)

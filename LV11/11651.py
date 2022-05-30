import sys
input = sys.stdin.readline

n = int(input())
l = []

for _ in range(n):
    x, y = map(int, input().split())
    l.append([y, x])
    
l.sort()

for i in l:
    print(i[1], i[0])

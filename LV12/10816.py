import sys
input = sys.stdin.readline
 
c = [0] * 20000001
 
n = int(input())
in1 = list(map(int, input().split()))
for i in in1:
    c[i+10000000] += 1
 
m = int(input())
in2 = list(map(int, input().split()))
r = [0] * m
for i in range(m):
    r[i] = c[in2[i]+10000000]
 
for i in r:
    print(i, end=' ')

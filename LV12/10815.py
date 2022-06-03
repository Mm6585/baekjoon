import sys
input = sys.stdin.readline
 
l = [0] * 20000001
 
n = int(input())
c = list(map(int, input().split()))
for i in c:
	l[i+10000000] += 1
 
m = int(input())
nums = list(map(int, input().split()))
 
r = [1 if l[i+10000000] else 0 for i in nums]
for i in r:
	print(i, end=' ')

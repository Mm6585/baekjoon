import sys
input = sys.stdin.readline

n = int(input())
l = []

for _ in range(n):
    v = input()
    age = int(v.split()[0])
    name = v.split()[1]
    l.append([age, name])

l.sort(key=lambda x : x[0])
    
for i in l:
	print(i[0], i[1])

import sys

input = sys.stdin.readline
n = int(input())
l = []
m = [0] * 8002
sum = 0
k = []

for _ in range(n):
    i = int(input())
    l.append(i)
    sum += i
l.sort()

avg = round(sum / len(l))

if (len(l) % 2 == 0):
    median = (l[len(l)//2-1] + l[len(l)//2]) / 2
else:
    median = l[len(l)//2]

for i in l:
    m[i+4000] += 1
j = max(m)
for i in range(len(m)):
    if (j <= m[i]):
        j = m[i]
        k.append(i - 4000)
k.sort()
if (len(k) > 1):
    k[0] = k[1]

print(avg)
print(median)
print(k[0])
print(max(l)-min(l))

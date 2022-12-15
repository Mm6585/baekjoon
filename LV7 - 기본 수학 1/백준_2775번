import sys

t = int(input())

for _ in range(t):
    n = int(sys.stdin.readline())
    k = int(sys.stdin.readline())
    cur = list(range(1, k+1))
    
    for _ in range(n):
        under = cur
        for i in range(1, k):
            cur[i] = cur[i-1] + under[i]
    
    print(cur[k-1])

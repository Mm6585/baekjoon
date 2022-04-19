s = input()
n = len(s)
result = [-1 for i in range(ord('z')-ord('a')+1)]

for i in range(n):
    x = ord(s[i])
    idx = s.index(s[i])
    
    for j in range(ord('a'), ord('z')+1):
        if (x == j):
            result[j-ord('a')] = idx
            break

for i in range(ord('z')-ord('a')+1):
    print(result[i], end=' ')

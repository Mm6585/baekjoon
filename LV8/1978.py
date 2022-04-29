n = int(input())
a = list(map(int, input().split()))
cnt = 0

for i in range(n):
    if (a[i] > 1):
        for j in range(2, a[i]):
            if (a[i] % j == 0):
                cnt -= 1
                break
        cnt += 1
            
print(cnt)

# Time Limit Exceeded
while (True):
    n = int(input())
    if (n == 0):
        break
    cnt = 0
    
    if (n > 1):
        for i in range(n+1, 2*n+1):
            k = 0
            for j in range(2, int(i**0.5)+1):
                if (i % j == 0):
                    k = 1
                    break
            if (k != 1):
                cnt += 1
        print(cnt)
    else:
        print(1)
        
        
# Accepted
num_list = list(range(2, 123456*2+1))
prime_list = []
for i in num_list:
    k = 0
    for j in range(2, int(i**0.5)+1):
        if (i % j == 0):
            k = 1
            break
    if (k == 0):
        prime_list.append(i)

while (True):
    n = int(input())
    if (n == 0):
        break
    cnt = 0
    
    for i in prime_list:
        if (n < i <= 2*n):
            cnt += 1
    
    print(cnt)

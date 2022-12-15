a, b = map(int, input().split())

for n in range(a, b+1):
    if (n == 1):
        continue
    else:
        check = 0
        for i in range(2, int(n**0.5)+1):
            if (n % i == 0):
                check = 1
                break
        if (check == 0):
            print(n)

def hanoi(x, a, b, c):
    if (x == 1):
        print(a, c)
    else:
        hanoi(x-1, a, c, b)
        print(a, c)
        hanoi(x-1, b, a, c)

n = int(input())
print(2**n-1)
hanoi(n, 1, 2, 3)

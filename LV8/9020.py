import sys

def make_prime_list(prime_list):
    for i in range(2, 10000):
        k = 0
        for j in range(2, int(i**0.5)+1):
            if(i % j == 0):
                k = 1
                break
        if (k == 0):
            prime_list.append(i)
        
def min_diff(n, prime_list):
    l = len(prime_list)
    result = 0
    min = 10000
    
    for i in range(int(l*n/20000), l+1):      # 반복 횟수를 줄이기 위해 입력값/2/10000의 비율로 소수 리스트의 시작점을 지정함.
        if (prime_list[i] >= n//2+1):
            break
        if (n-prime_list[i] in prime_list):
            if (min > n-2*prime_list[i]):
                min = n-2*prime_list[i]
                result = prime_list[i]

    return result, n-result

prime_list = []
make_prime_list(prime_list)

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    result = min_diff(n, prime_list)
    print(result[0], result[1])

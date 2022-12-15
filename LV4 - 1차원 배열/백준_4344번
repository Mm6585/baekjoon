c = int(input())

for i in range(c):
    tmp = list(map(int, input().split()))
    n = tmp[0]
    scores = tmp[1:]
    mean = sum(scores) / n
    result = [1 for x in scores if x>mean]
    print('%.3f' % (sum(result) / n * 100) + '%')

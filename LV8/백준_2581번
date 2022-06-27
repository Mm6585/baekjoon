start = int(input())
end = int(input())
result = []

for i in range(start, end+1):
    if (i == 2):
        result.append(i)
    for j in range(2, i):
        if (i % j == 0):
            break;
        elif (j == i-1):
            result.append(i)

if (len(result) != 0):
    print(sum(result))
    print(min(result))
else:
    print(-1)

year = int(input())
r = year % 400
if (r == 0):
    result = 1
else:
    r = r % 100
    if (r == 0):
        result = 0
    else:
        r = r % 4
        if (r == 0):
            result = 1
        else:
            result = 0
print(result)

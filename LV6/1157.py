from collections import Counter
s = input()
s = s.upper()

count = Counter(s).most_common()
result = count[0][0]
max = count[0][1]
for i in range(1, len(count)):
    if (max == count[i][1]):
        result = '?'
        break

print(result)

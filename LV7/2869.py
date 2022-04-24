import math
a, b, v = map(int, input().split())
n = int(math.ceil((v-a) / (a-b))) + 1
print(n)

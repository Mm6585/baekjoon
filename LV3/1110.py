n = int(input())
cnt = 0
result = n

while (True):
  cnt+=1
  a = result // 10
  b = result % 10
  c = a + b
  result = (b*10) + (c%10)
  if (n == result):
    break

print(cnt)

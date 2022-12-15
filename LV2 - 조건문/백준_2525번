h, m = map(int, input().split())
time = int(input())
th = (m + time) // 60
tm = (m + time) % 60

if (m+time >= 60):
    m = tm
    if (h+th >= 24):
        h = h + th - 24
    else:
        h = h + th
else:
    m = m + time

print(h, m)

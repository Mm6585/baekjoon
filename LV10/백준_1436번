n = int(input())
cnt = 0
i = 666
n_list = []
while (True):
    s = str(i)
    s_cnt = 0
    for j in range(1, len(s)):
        if (s[j] == '6' and s[j] == s[j-1]):
            s_cnt += 1
        else:
            s_cnt = 0
        if (s_cnt == 2):
            n_list.append(int(s))
            break
    if (len(n_list) == n):
        break
    i += 1
print(n_list[n-1])

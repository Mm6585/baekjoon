cro_alp = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()
cnt = 0

i = 0
while (i < len(s)):
    flag = 0
    for j in range(len(cro_alp)):
        if (s[i:i+len(cro_alp[j])] == cro_alp[j]):
            flag = 1
            cnt += 1
            i += len(cro_alp[j])-1
            if (i >= len(s)):
                break
    if (flag == 0):
        cnt += 1
    i += 1

print(cnt)

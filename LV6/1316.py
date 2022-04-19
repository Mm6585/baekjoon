def continuous_length(array, index, length=1):
    if (index < len(array)-1):
        if (array[index]==array[index+1]):
            return length + continuous_length(array, index+1, length)
    return length


def group_checker(s):
    check_list = []

    i = 0
    while (i < len(s)):
        if (check_list.count(s[i]) != 0):
            return 0
        check_list.append(s[i])
        l = continuous_length(s, i)
        if (l != 0):
            i += l
        else:
            i += 1

    return 1


n = int(input())
cnt = 0

for i in range(n):
    s = input()
    cnt += group_checker(s)

print(cnt)

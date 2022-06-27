# 1
import sys

input = sys.stdin.readline
n = int(input())
l = []

for _ in range(n):
    l.append(int(input()))
l.sort()

for i in l:
    print(i)
    
    
# 2
# merge sort
# pypy3
def merge(num_list, sort_list, left, mid, right):
    i = left
    j = mid + 1
    k = left
    
    while ((i <= mid) and (j <= right)):
        if (num_list[i] < num_list[j]):
            sort_list[k] = num_list[i]
            i += 1
            k += 1
        else:
            sort_list[k] = num_list[j]
            j += 1
            k += 1
    if (i > mid):
        while (j <= right):
            sort_list[k] = num_list[j]
            j += 1
            k += 1
    else:
        while (i <= mid):
            sort_list[k] = num_list[i]
            i += 1
            k += 1
    for i in range(left, right+1):
        num_list[i] = sort_list[i]
            
def merge_sort(num_list, sort_list, left, right):
    if (left < right):
        mid = (left + right) // 2
        merge_sort(num_list, sort_list, left, mid)
        merge_sort(num_list, sort_list, mid+1, right)
        merge(num_list, sort_list, left, mid, right)
        
import sys

input = sys.stdin.readline
n = int(input())
l = []
s = list(range(n))

for _ in range(n):
    l.append(int(input()))

merge_sort(l, s, 0, len(l)-1)

for i in l:
    print(i)

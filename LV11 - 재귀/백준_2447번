def stars(x):
    if (x == 1):
        return ('*')
    
    star = stars(x//3)
    star_list = []

    for s in star:
        star_list.append(s*3)
    for s in star:
        star_list.append(s + ' '*(x//3) + s)
    for s in star:
        star_list.append(s*3)
        
    return star_list

n = int(input())
print('\n'.join(stars(n)))

def d(n):
    n_s = n
    for i in str(n):
        n_s += int(i)
    return n_s

def d2(n):
    li = []
    result = []
    for i in range(1, n+1):
        li.append(i)
        i_s = i
        for j in str(i):
            i_s += int(j)
        result.append(i_s)
    for k in result:
        if k in li:
            li.remove(k)
    return li

list = d2(10000)
for i in list:
    print(i)
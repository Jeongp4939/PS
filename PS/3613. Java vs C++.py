# https://www.acmicpc.net/problem/3613

name = input()
li=[]
li_2 = []
flag = 0

if '_' in name:
    if '__' in name:
        print('Error!')
        exit()
    li = name.split('_')
    for i in range(len(li)):
        if i == 0:
            li_2.append(li[i])
        else:
            li_2.append(li[i][0].upper()+li[i][1:])
    print(''.join(li_2))
else:
    for i in name:
        if i.isupper():
            flag=1
            li_2.append('_' + i.lower())
        else:
            li_2.append(i)

    if flag:
        print(''.join(li_2))
    else:
        print('Error!')

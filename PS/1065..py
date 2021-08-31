def func(n):
    cnt = 0
    for i in range(1,n+1):
        if i < 100:
            cnt += 1
        elif i%10 + i//100 == ((i//10)%10)*2:
            cnt += 1
    return cnt

print(func(int(input())))
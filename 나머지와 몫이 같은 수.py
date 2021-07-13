def solution():
    n = int(input())
    if n == 1:
        return 0
    else:
        li = []
        for i in range(1, n):
            li.append(i * (n + 1))
        return sum(li)
        # res=0
        # for i in range(1, n):
        #     res += i * (n + 1)

    # (n + 1) * n * (n - 1) / 2 # 축약 가능(가우시안합)


print(solution())

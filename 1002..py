n = int(input())
for _ in range(n):
    test_case = list(map(int, input().split()))
    distance = (test_case[0] - test_case[3])**2 + (test_case[1] - test_case[4])**2

    r1 = test_case[2]
    r2 = test_case[5]

    if distance == 0:
        if r1 == r2:                                                # 두 원이 같은 경우(무한대)
            print(-1)
        else:                                                       # 두 원이 만나지 않는 경우
            print(0)
    else:
        if (r1+r2)**2 == distance or (r1 - r2)**2 == distance:      # 두 원이 접하는 경우
            print(1)

        elif (r1-r2)**2 > distance or (r1+r2)**2 < distance:        # 두 원이 만나지 않는 경우
            print(0)

        else:                                                       # 두 원이 두 점에서 만나는 경우
            print(2)
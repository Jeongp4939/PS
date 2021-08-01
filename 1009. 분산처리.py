# T = int(input())
#
# for _ in range(T):
#     a, b = map(int, input().split())
#
#     if a**b %10 == 0:
#         print(10)
#     else:
#         print(a**b%10)
#==================시간초과===========================

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())

    if pow(a, b, 10) == 0:
        print(10)
    else:
        print(pow(a,b,10))

#=====================통과(128ms)==============================

# t = int(input())
# li=[]
# for i in range(t):
#     a,b=input().split()
#     li.append((int(a),int(b)))
#
# for i in li:
#     if i[0]%10==0:
#         print(10)
#     else:
#         print(pow(i[0],i[1],10))

#======================통과(80ms)===============================
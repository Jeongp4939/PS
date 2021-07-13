n = int(input())
for i in range(1, n+1):
    if n % i == 0:
        print(i, end=' ')
# O(n)

# n = int(input())
# sqrt_n = int(n ** (1/2))
# 
# front_divisor_list = []
# rear_divisor_list = []
# 
# for i in range(1, sqrt_n+1):
#     if num % i ==0:
#         front_divisor_list.append(i)
#         if i != int(n/i):
#             rear_divisor_list.append(int(n/i))
#             
# print(front_divisor_list + rear_divisor_list[::-1])
# 강사님 코드 O(n^(1/2))

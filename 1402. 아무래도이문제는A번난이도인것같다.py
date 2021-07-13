# n, n_prime = map(int, input().split())
#
# prime_factor = []
# while n%2 == 0:
#     prime_factor.append(2)
#     n /= 2
#
# for i in range(3, int(n**(1/2))+1, 2):
#     while n%i == 0:
#         prime_factor.append(int(i))
#         n /= i
# if n > 2:
#     prime_factor.append(int(n))
#
# if sum(prime_factor) == n_prime:
#     print("yes")
# else:
#     print("no")

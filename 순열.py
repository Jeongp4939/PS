factorial_memo = {}
def factorial(n):
    if n < 2:
        return 1
    if n not in factorial_memo:
        factorial_memo[n] = n * factorial(n-1)
    return factorial_memo[n]


def permutation(n, r):
    return int(factorial(n)/factorial(r-1))


def combination(n, r):
    return int(factorial(n)/(factorial(r)*factorial(n-r)))


def combination2(n, r):
    return int(combination(n-1, r-1) + combination(n-1, r))


print(permutation(5, 3))
print(combination(10, 3))


factorial_memo = {}
def factorial(n):
    if n < 2:
        return 1
    if n not in factorial_memo:
        factorial_memo[n] = n * factorial(n-1)
    return factorial_memo[n]

def combination(n, r):
    return int(factorial(n)/(factorial(r)*factorial(n-r)))

a, b = map(int, input().split())
print(combination(a,b))
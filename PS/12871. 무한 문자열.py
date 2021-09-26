# https://www.acmicpc.net/problem/12871
import math
def lcm(a,b):
    return a*b//math.gcd(a,b)
s = input()
t = input()

len_s = len(s)
len_t = len(t)
len_common = lcm(len_s, len_t)

s = (len_common//len_s) * s
t = (len_common//len_t) * t

if s == t:
    print(1)
else:
    print(0)


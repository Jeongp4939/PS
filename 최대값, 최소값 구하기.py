li = list(map(int, input().split()))

# for i in range(len(li)):
#     for j in range(i+1, len(li)):
#         if li[i] > li[j]:
#             li[i], li[j] = li[j], li[i]
# print(li)
# print(li[-1], li[0])
# O(n^2)
max_n = li[0]
min_n = li[0]

for i in li:
    if i > max_n:
        max_n = i
    if i < min_n:
        min_n = i

print(max_n, min_n)
# O(N)

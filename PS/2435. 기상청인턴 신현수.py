n, k = map(int, input().split())
temp_list = list(map(int, input().split()))
temp_sum =[]

for i in range(n-k+1):
    # print(temp_list[i:i+k], i, i+k)
    temp_sum.append(sum(temp_list[i:i+k]))
# print(temp_sum)
print(max(temp_sum))
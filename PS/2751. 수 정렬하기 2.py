def merge_sort(list):
    list_length = len(list)
    if list_length <= 1:
        return list

    mid_idx = list_length // 2

    left_partition = merge_sort(list[:mid_idx])
    right_partition = merge_sort(list[mid_idx:])

    return merge(left_partition, right_partition)

def merge(left, right):
    output = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1
    output.extend(left[i:])
    output.extend(right[j:])

    return output


n = int(input())
li = []
for _ in range(n):
    li.append(int(input()))

result = merge_sort(li)

for i in result:
    print(i)


# ==========================================================

# import sys
#
# a = int(input())
# num = []
# for _ in range(a):
#     num.append(int(sys.stdin.readline()))
#
# for i in sorted(num):
#     sys.stdout.write(str(i) + "\n")

# ==========================================================
# 4 3 7 2 5 0 6 1
# 34 27 05 16
# 2347 0156
# 01234567

#merge sor top down recursion


# def merge_sort(start_idx, end_idx, num_list):
#     if start_idx == end_idx:
#         return num_list[start_idx:end_idx+1]
#
#     mid_idx = (start_idx+end_idx)//2
#
#     f_sorted_list = merge_sort(start_idx, mid_idx, num_list) # front
#     b_sorted_list = merge_sort(mid_idx+1, end_idx, num_list) # back
#
#     f_idx = 0
#     b_idx = 0
#     combined_list = []
#
#     while f_idx < len(f_sorted_list) and b_idx < len(b_sorted_list):
#         if f_sorted_list[f_idx] < b_sorted_list[b_idx]:
#             combined_list.append(f_sorted_list[f_idx])
#             f_idx += 1
#         else:
#             combined_list.append(b_sorted_list[b_idx])
#             b_idx += 1
#
#     return combined_list + f_sorted_list[f_idx:] + b_sorted_list[b_idx:]
#
# n = int(input())
# num_list = []
#
# for _ in range(n):
#     num_list.append(int(input()))
#
# for num in merge_sort(0, n-1, num_list):
#     print(num)


# ========================================================

#merge sort bottom up  recursion




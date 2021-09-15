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

#merge sort top down recursion


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


# ==========================================================

# merge sort bottom up recursion

# 43725061
# 4372 5061
# 43 72 50 61
# 4 3 7 2 5 0 6 1
# 34 27 05 16
# 2347 0156
# 01234567

# 5 4 3 2 1
# 45 23 1
# 2345 1
# 12345

# n = int(input())
# num_list = []
#
# for _ in range(n):
#     num_list.append(int(input()))
#
# target_size = 1
#
# while target_size < n:
#     start_idx = 0
#
#     while start_idx < n:
#         mid_idx = min(start_idx + target_size - 1, n - 1)
#         end_idx = min(mid_idx + target_size, n - 1)
#
#         f_idx = start_idx
#         b_idx = mid_idx + 1
#         combined_list = []
#
#         while f_idx <= mid_idx and b_idx <= end_idx:
#             if num_list[f_idx] < num_list[b_idx]:
#                 combined_list.append(num_list[f_idx])
#                 f_idx += 1
#             else:
#                 combined_list.append(num_list[b_idx])
#                 b_idx += 1
#
#         combined_list = combined_list + num_list[f_idx:mid_idx + 1] + num_list[b_idx:end_idx + 1]
#         # print(combined_list)
#
#         num_list[start_idx:end_idx + 1] = combined_list
#         start_idx = end_idx + 1
#
#     # start_idx ~ mid_idx
#     # mid_idx+1 ~ end_idx
#
#     target_size *= 2
#
# for num in num_list:
#     print(num)






# ========================================================
#
# def quick_sort(num_list):
#     if len(num_list) <= 1:
#         return num_list
#
#     pivot_idx = 0
#
#     less_list = []
#     more_list = []
#
#     for num in num_list[pivot_idx + 1:]:
#         if num < num_list[pivot_idx]:
#             less_list.append(num)
#         else:
#             more_list.append(num)
#
#     # print(f"{less_list}, {[num_list[pivot_idx]]}, {more_list}")
#
#     return quick_sort(less_list) + [num_list[pivot_idx]] + quick_sort(more_list)
#
#
# n = int(input())
# num_list = []
#
# for _ in range(n):
#     num_list.append(int(input()))
#
# for num in quick_sort(num_list):
#     print(num)

# ========================================================================
#
# def quick_sort_inplace(start_idx, end_idx, num_list):
#     if end_idx - start_idx + 1 <= 1:
#         return
#
#     pivot_idxes = [
#         start_idx,
#         end_idx,
#         (start_idx + end_idx) // 2
#     ]
#
#     pivot_values = []
#
#     for idx in pivot_idxes:
#         pivot_values.append(num_list[idx])
#
#     mid_val = sum(pivot_values) - max(pivot_values) - min(pivot_values)
#     mid_idx = pivot_idxes[pivot_values.index(mid_val)]
#
#     num_list[start_idx], num_list[mid_idx] = num_list[mid_idx], num_list[start_idx]
#
#     pivot_idx = start_idx
#     f = start_idx + 1
#     r = end_idx
#
#     while f <= r:
#         while num_list[r] > num_list[pivot_idx]:
#             r -= 1
#
#         while f <= r and num_list[f] < num_list[pivot_idx]:
#             f += 1
#
#         if f <= r:
#             num_list[f], num_list[r] = num_list[r], num_list[f]
#
#         print(num_list)
#
#     num_list[r], num_list[pivot_idx] = num_list[pivot_idx], num_list[r]
#
#     quick_sort_inplace(start_idx, r - 1, num_list)
#     quick_sort_inplace(r + 1, end_idx, num_list)
#
#
# n = int(input())
# num_list = []
#
# for _ in range(n):
#     num_list.append(int(input()))
#
# quick_sort_inplace(0, n - 1, num_list)
#
# for num in num_list:
#     print(num)
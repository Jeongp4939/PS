# https://www.acmicpc.net/problem/1920

def binary_search(arr, target, low, high):
    if low > high:
        return 0
    mid_idx = (low + high)//2
    if arr[mid_idx] > target:
        return binary_search(arr, target, low, mid_idx-1)
    elif arr[mid_idx] < target:
        return binary_search(arr, target, mid_idx+1, high)

    return 1

n = int(input())
n_list = sorted(list(map(int, input().split())))
m = int(input())
m_list = list(map(int, input().split()))

for i in range(m):
    if binary_search(n_list, m_list[i], 0, n-1):
        print(1)
    else:
        print(0)


# ========================================================

# n = int(input())
# num_list = list(map(int,input().split()))
# num_list.sort() # n log n => 100000 log 100000 => 1660964...
#
# m = int(input())
#
# for target_num in map(int, input().split()): #100000
#     # 0 1 2 3 4 5 6
#     # 0 1 2 3
#
#     start_idx = 0
#     end_idx = n - 1
#     find_result = 0
#
#     while start_idx <= end_idx:
#         mid_idx = (start_idx + end_idx) // 2
#
#         if num_list[mid_idx] > target_num:
#             end_idx = mid_idx - 1
#         elif num_list[mid_idx] < target_num:
#             start_idx = mid_idx + 1
#         else:
#             find_result = 1  # print(mid_idx)
#             break
#     print (find_result)

# ========================================================
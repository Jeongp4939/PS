import time

start = time.time()

def binary_search(arr, target, low=None, high=None):
    low, high = low or 0, high or len(arr) - 1
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] > target:
        return binary_search(arr, target, low, mid)
    if arr[mid] == target:
        return mid
    if arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)

print(binary_search(["0","1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"], "8"))

print("time : {}".format(time.time()-start))
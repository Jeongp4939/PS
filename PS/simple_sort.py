def insertion_sort(lst):
    sorted_list = lst.copy()
    for i in range(len(sorted_list)):
        for j in range(i):
            if sorted_list[i-j] < sorted_list[i-j-1]:
                sorted_list[i-j-1], sorted_list[i-j] = sorted_list[i-j], sorted_list[i-j-1]
                print(sorted_list)
    return sorted_list

def selection_sort(lst):
    sorted_list = lst.copy()
    for i in range(len(sorted_list)):
        min_idx = sorted_list.index(min(sorted_list[i:]))
        sorted_list[i], sorted_list[min_idx] = sorted_list[min_idx], sorted_list[i]
        print(sorted_list)
    return sorted_list

def bubble_sort(lst):
    sorted_list = lst.copy()
    for i in range(len(sorted_list)):
        for j in range(len(sorted_list) - i - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
            print(sorted_list)
    return sorted_list

n = int(input())
num_list = []

for _ in range(n):
    num = int(input())
    num_list.append(num)

insertion_sorted_list = insertion_sort(num_list)
print(" ".join(map(str, insertion_sorted_list)))
print('==========================================')
selection_sorted_list = selection_sort(num_list)
print(" ".join(map(str, selection_sorted_list)))
print('==========================================')
bubble_sorted_list = bubble_sort(num_list)
print(" ".join(map(str, bubble_sorted_list)))

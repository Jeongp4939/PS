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
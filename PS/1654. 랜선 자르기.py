
k, n = map(int, input().split())    # 다시 공부 필요
li = []
while k:
    li.append(int(input()))
    k -= 1
left, right = 1, max(li)
while left <= right:    # 이진 탐색트리를 이용한 적절한 길이 찾기
    mid = (left + right)//2
    lines = 0
    for i in li:
        lines += i//mid
    if lines >= n:
        left = mid + 1
    else:
        right = mid - 1
print(right)


# 첫째 줄에 트리의 노드의 개수 N이 주어진다. N은 50보다 작거나 같은 자연수이다.
# 둘째 줄에는 0번 노드부터 N-1번 노드까지, 각 노드의 부모가 주어진다.
# 만약 부모가 없다면 (루트) -1이 주어진다. 셋째 줄에는 지울 노드의 번호가 주어진다.

n = int(input())
arr = list(map(int, input().split()))
remove_node = int(input())

tree = {}


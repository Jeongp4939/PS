# https://www.acmicpc.net/problem/2422

# 조합..?

n, m = map(int, input().split())
m_list=[]
for _ in range(m):
    m_list.append(list(map(int, input().split())))
print(m_list)



# 병국 코드
# N, M = map(int, input().split())                            # 아이스크림의 종류와 섞으면 안되는 조합의 수를 받는다.
# not_mix = {i:set() for i in range(1, N+1)}                  # 아이스크림의 수만큼 1~N가지 딕셔너리를 만들어놓는다.
# cnt = 0                                                     # 조합 가능한 수
# for _ in range(M):                                          # 섞으면 안되는 조합을 받기위해 for문을 돌린다.
#     a, b = map(int, input().split())                        # 섞으면 안되는 조합
#     not_mix[a].add(b)                                       # a에 b를 b에 a를 넣어준다.
#     not_mix[b].add(a)
# for i in range(1, N-1):                                     # 3가지를 섞는데 순서는 상관없으므로 첫번째 아이스크림은 1~N-2까지
#     for j in range(i+1, N):                                 # 두번째 아이스크림은 i+1~N-1까지 세번째는 j+1~N까지 이다
#         if j in not_mix[i]:                                 # 만약 j맛이 i와 섞으면 안되는 맛이라면 다음 맛으로 넘어간다.
#             continue
#         for k in range(j+1, N+1):
#             if k in not_mix[i] or k in not_mix[j]:          # 만약 k맛이 i나 j와 섞으면 안되는 맛이라면 넘어간다.
#                 continue
#             cnt += 1                                        # 모두 만족하면 섞어도 되는 맛에 +1을 해준다.
# print(cnt)                                                  # 출력
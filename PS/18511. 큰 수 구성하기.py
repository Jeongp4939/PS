# 백준 18511. 큰 수 구성하기
# 10 <= N <= 100000000, 1<= len(K_list) <=3
pass
#========================실패============================
# def make_biggest(num_list, big , n):    # 자리수 별 크기 비교, 최고자리 수가 같을 때만 검사, 다음 수가 작으면 그 뒤는 모두 최대 숫자로 통일
#     digit = len(str(n))             # N의 자리수
#     if not 0 in [i > n//10**(digit-1) for i in num_list]: # list 내부에 n의 최고자리 수보다 작거나 같은 수가 존재하지 않을때.
#         for i in num_list:
#             big += i * 10 ** (digit - 2)
#             for j in range(digit - 2):
#                 big += num_list[0] * 10 ** j
#             return int(big)
#     else:
#         for i in num_list:                      # 내림차순 정렬 된 리스트
#             if n//10**(digit-1) == i:           # n의 최고 자리수 비교
#                 big += i * 10 ** (digit - 1)
#                 n %= 10 ** (digit - 1)          # n의 최고 자리수 제거
#                 return make_biggest(num_list, big, n)
#             elif n//10**(digit-1) > i:          # 최고 자리수의 숫자가 n보다 작으면 그 이후 숫자는 비교할 필요 없음
#                 big += i * 10 ** (digit - 1)
#                 for j in range(digit-1):
#                     big += num_list[0]*10**j
#                 return int(big)
#
# N, K = map(int, input().split())
# numbers = list(map(int, input().split()))
# numbers.sort(reverse=True)   # 내림차순 정렬
#
# biggest_num = 0
#
# print(make_biggest(numbers, biggest_num, N))
#============================================================================

# n, k = input().split()
# num_list = list(map(int, input().split()))
#
# num_list.sort(reverse=True)
#
# answer = 0
# def make_biggest(n, num_list, answer):
#     i = 0
#     digit = len(str(n))
#     while digit:
#         for j in range(len(num_list)):
#             if answer + num_list[j] * (10 ** i) < int(n):
#                 answer += num_list[j] * (10 ** i)
#                 digit -= 1
#                 break
#             if answer + num_list[j] * (10 ** i) > int(n):
#                 return answer
#         i += 1
#     return answer
# print(make_biggest(n, num_list, answer))

#===========================================================================

# def backtracking(num, cnt):                         # 현재 숫자와 몇 번째 자리까지 계산했는지 입력 받는다.
#     global max_num                                  # 최대값을 계속 갱신해줘야 되므로 전역화 해준다.
#     if cnt > len(str(N)):                           # cnt가 N의 길이보다 커졌다는 것은 이미 num이 N보다
#         return                                      # 값이 크다는 것을 의미하기 때문에 return 하여 종료한다.
#     if num > N:                                     # 만약 num값이 N보다 커져도 종료한다.
#         return
#     else:                                           # num이 N보다 작으면 max_num을 비교하여 더 큰값을 저장해 준다.
#         max_num = max(max_num, num)
#     for e in element:                               # 요소를 한개씩 꺼내준다.
#         backtracking(num + e * 10**cnt, cnt+1)      # num에 각자리의 수를 더해주고, cnt를 1 증가시켜서
#                                                     # backtracking 함수를 재귀로 다시 실행시켜준다.
# N, K = map(int, input().split())                    # N과 K값을 받아온다.
# element = list(map(int, input().split()))           # K개의 요소를 리스트에 저장해 준다.
# max_num = 0                                         # 요소의 값중 가장 큰 값을 출력해야하므로 변수를 만들어준다.
# backtracking(0, 0)                                  # backtracking 함수의 초기값은 0, 0으로 넣어준다.
# print(max_num)                                      # 함수가 종료되면 가장 큰 max_num을 출력해준다.

#===========================================================================
#
# import itertools
# maximum, N = map(int, input().split())
# len_max = len(str(maximum))
# elements = list(map(int, input().split()))
# elements.sort(reverse=True)
# len_numbers = len(elements)
# cnt = 0
# while not cnt:
#     case = list(itertools.product(elements, repeat=len_max))
#     for i in case:
#         num = ''.join(map(str, i))
#         if maximum >= int(num):
#             print(num)
#             cnt = 1
#             break
#     len_max -= 1
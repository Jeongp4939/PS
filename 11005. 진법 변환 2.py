# def operation(N, B, answer):
#     if N == 0:
#         answer = answer[::-1]
#         return answer
#     char_map_str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # 10진법이면 9 까지, 36진법이면 Z까지 표현된다
#     answer += str(char_map_str[N % B])  # 위치로 진법 변환
#     N //= B
#     return operation(N, B, answer)
#
# N, B = map(int, input().split())
# print(operation(N, B, ''))


#======================================================

# n, b = map(int, input().split())
#
# result_list = []
# q = n
#
# while q > 0:
#     q, r = divmod(q, b)
#
#     if r < 10:
#         result_list.append(r)
#     else:
#         result_list.append(chr(r - 10 + ord('A')))
#
# print("".join(result_list[::-1]))

#===================== recursion ========================
#
# def convert_from_dec(q, b):
#     if q == 0:
#         return ''
#
#     q, r = divmod(q, b)
#
#     if r < 10:
#         char_str = str(r)
#     else:
#         char_str = chr(r-10+ord('A'))
#
#     return convert_from_dec(q, b) + char_str
#
# n, b = map(int, input().split())
# print(convert_from_dec(n, b))

#========================================================

# def convert_from_dec_map(q, b, char_num_map):
#     if q == 0:
#         return ""

#     q, r = divmod(q, b)
#     return convert_from_dec_map(q, b, char_num_map) + char_num_map[r]

# char_num_map = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# n, b = map(int, input().split())
# print(convert_from_dec_map(n, b, char_num_map))
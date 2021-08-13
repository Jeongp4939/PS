# def operation(N, B, answer):
#     if N ==0:
#         answer = answer[::-1]
#         return answer
#     system = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # 10진법이면 9 까지, 36진법이면 Z까지 표현된다
#     answer += str(system[N % B])  # 위치로 진법 변환
#     N //= B
#     return operation(N, B, answer)
#
# N, B = map(int, input().split())
# print(operation(N, B, ''))


# def solution(numbers):
#     answer = ''
#     for i in range(len(numbers)):
#         numbers[i] = str(numbers[i])
#     numbers.sort(key=lambda x: x[0])
#     for i in range(len(numbers)-1):
#         for j in range(i+1, len(numbers)-1):
#             if numbers[i][0] == numbers[j][0]:
#                 if int(numbers[i]+numbers[j]) > int(numbers[j]+numbers[i]):
#                     numbers[i], numbers[j] = numbers[j], numbers[i]
#
#     for _ in range(len(numbers)):
#         answer += numbers.pop()
#     return answer
#
# print(solution([6, 10, 2]))

def solution(numbers):
    answer = ''
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])
    print(numbers)
    for _ in range(len(numbers)):
        answer += numbers.pop()
    return answer

print(solution([3, 30, 34, 5, 9]))

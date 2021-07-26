def solution(numbers):
    answer = ''
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])
    numbers.sort(key=lambda x: x[0])
    for _ in range(len(numbers)):
        answer += numbers.pop()
    return answer

print(solution([3, 30, 34, 5, 9]))
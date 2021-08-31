from itertools import permutations

def solution(numbers):
    answer = 0
    list_prime = []
    joined_list_prime = []
    for i in range(1, len(numbers)+1):
        list_prime += list(permutations(numbers, i))
    for i in range(len(list_prime)):
        joined_list_prime.append(int(''.join(list_prime[i])))
    joined_list_prime = list(set(joined_list_prime))

    for i in joined_list_prime:
        if int(i) < 2:
            continue
        for j in range(2, int(int(i)**(1/2))+1):
            if int(i) % j == 0:
                break
        else: answer += 1

    return answer

print(solution("17"))
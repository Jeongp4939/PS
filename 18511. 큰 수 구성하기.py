# 백준 18511. 큰 수 구성하기
# 10 <= N <= 100000000, 1<= len(K_list) <=3

def make_biggest(num_list, big , n):    # 자리수 별 크기 비교, 최고자리 수가 같을 때만 검사, 다음 수가 작으면 그 뒤는 모두 최대 숫자로 통일
    digit = len(str(n))             # N의 자리수
    if not 0 in [i > n//10**(digit-1) for i in num_list]: # list 내부에 n의 최고자리 수보다 작거나 같은 수가 존재하지 않을때.
        for i in num_list:
            big += i * 10 ** (digit - 2)
            for j in range(digit - 2):
                big += num_list[0] * 10 ** j
            return big
    else:
        for i in num_list:                      # 내림차순 정렬 된 리스트
            if n//10**(digit-1) == i:           # n의 최고 자리수 비교
                big += i * 10 ** (digit - 1)
                n %= 10 ** (digit - 1)          # n의 최고 자리수 제거
                return make_biggest(num_list, big, n)
            elif n//10**(digit-1) > i:          # 최고 자리수의 숫자가 n보다 작으면 그 이후 숫자는 비교할 필요 없음
                big += i * 10 ** (digit - 1)
                for j in range(digit-1):
                    big += num_list[0]*10**j
                return big

N, K = map(int, input().split())
k_list = list(map(int, input().split()))
k_list.sort(reverse=True)   # 내림차순 정렬

biggest_num = 0

print(make_biggest(k_list, biggest_num, N))
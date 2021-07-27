# 백준 18511. 큰 수 구성하기
# 10 <= N <= 100000000, 1<= len(K_list) <=3
N, K = map(int, input().split())
k_list = map(int, input().split())
k_list.sort()
# 최대로 만들 수 있는 숫자가 최고자리수의 숫자와 같을 때, 다음 숫자를 비교, 확실하게 큰 수라면 다음 수는 전부 MAX num 으로 만들수 있음

digit = len(str(N))     # n 이 몇자리 숫자인지 확인


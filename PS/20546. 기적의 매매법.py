# https://www.acmicpc.net/problem/20546
#
# 장기 투자를 지향하는 준현이는 한 번 산 주식은 절대 팔지 않는다.
# 주식 매수 후 오로지 기도만 하기 때문에 이를 BNP 전략이라고 한다.
# BNP는 Buy and Pray의 약자이다.
# 준현이는 주식을 살 수 있다면 무조건 최대한 많이 산다.
# 준현이는 욕심쟁이이기 때문에, 주식을 살 수 있다면 가능한 만큼 즉시 매수한다.

# 성민이는 주식이 타이밍 싸움이라 생각한다. 전형적인 단기 투자자로 생각하면 오산이다.
# 성민이만의 전략이 있기 때문이다. 이른바 33 매매법으로, 그 방법은 다음의 세 가지 룰로 이루어져있다.
# 모든 거래는 전량 매수와 전량 매도로 이루어진다.
# 현재 가지고 있는 현금이 100원이고 주가가 11원이라면 99원어치의 주식을 매수하는 것이다.
# 단, 현금이 100원 있고 주가가 101원이라면 주식을 살 수 없다. 성민이는 빚을 내서 주식을 하지는 않는다.
# 3일 연속 가격이 전일 대비 상승하는 주식은 다음날 무조건 가격이 하락한다고 가정한다.
# 따라서 현재 소유한 주식의 가격이 3일째 상승한다면, 전량 매도한다. 전일과 오늘의 주가가 동일하다면 가격이 상승한 것이 아니다.
# 3일 연속 가격이 전일 대비 하락하는 주식은 다음날 무조건 가격이 상승한다고 가정한다.
# 따라서 이러한 경향이 나타나면 즉시 주식을 전량 매수한다. 전일과 오늘의 주가가 동일하다면 가격이 하락한 것이 아니다.

money_base = int(input())                   # 시작 금액
stock_price = list(map(int, input().split()))     # 일자별 주식 가격
june_price, sung_price = money_base, money_base   # 동일한 시작 금액
june_stock, sung_stock = 0, 0                     # 시작시 주식 보유량
flag = []
# 준현 : 보유가보다 주식의 가격이 낮을때 살 수 있는 만큼 전부 구매/ 팔지 않음
for i in range(len(stock_price)):
    june_stock += (june_price // stock_price[i])
    june_price -= (june_price // stock_price[i]) * stock_price[i]

june_price = june_price + june_stock * stock_price[len(stock_price)-1]  # 마지막 날의 자산
# print(june_price + june_stock * stock_price[len(stock_price)-1])

# 성준 : 주식이 3일 연속 상승 : 전량 매도, 주식이 3일 연속 하락: 전량 매수
for i in range(len(stock_price)):
    if i >=1:                                               # flag 로 전일과 주식 가격을 비교 오르면 1, 내리면 0
        if stock_price[i-1] < stock_price[i]:
            flag.append(1)
        elif stock_price[i-1] > stock_price[i]:
            flag.append(0)
        else:
            flag.append('-')

    if len(flag)>=3:
        if flag[-3:] == [1, 1, 1]:                          # 3일 뒤 두터 전일 3일의 오르고 내림 확인
            sung_price += sung_stock * stock_price[i]
            sung_stock = 0                                  # 전량 매도 하므로 주식보유 -> 0
        elif flag[-3:] == [0, 0, 0]:
            sung_stock += sung_price // stock_price[i]
            sung_price -= (sung_price // stock_price[i]) * stock_price[i]
        else:
            pass
sung_price = sung_price + sung_stock * stock_price[len(stock_price)-1]   # 마지막 날의 자산
# print(i, sung_price + sung_stock * stock_price[len(stock_price)-1] )

# 결과 출력
if june_price > sung_price:
    print('BNP')
elif june_price < sung_price:
    print('TIMING')
else:
    print('SAMESAME')
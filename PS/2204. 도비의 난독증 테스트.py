# https://www.acmicpc.net/problem/2204

while 1:
    n = int(input())
    word_li = []

    if not n: break

    for _ in range(n):
        word_li.append(input())
    word_li.sort(key=lambda x: x.upper())
    print(word_li[0])



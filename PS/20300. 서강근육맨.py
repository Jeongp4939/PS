N = int(input())
loss = list(map(int, input().split()))
M = 0

loss.sort()

if N%2==0:
    for i in range(len(loss)//2):
        M = max(M, loss[i] + loss[N-i-1])
else:
    for i in range(len(loss) // 2):
        M = max(M, loss[i] + loss[N - i - 2])
    M = max(M, loss[-1])
print(M)
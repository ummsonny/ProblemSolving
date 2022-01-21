n = int(input())

array = [int(input()) for _ in range(n)]
result = sorted(array, reverse=True)

for i in result:
    print(i, end=' ')
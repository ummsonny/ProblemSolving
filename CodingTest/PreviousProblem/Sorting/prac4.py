# 핵심아이디어 : 최소2개의 숫자를 계속 합치면 된다.
import heapq

n = int(input())

heap=[]

for _ in range(n):
    data = (int(input()))
    heapq.heappush(heap, data)

result = 0

while len(heap) != 1:

    one = heapq.heappop(heap)
    two = heapq.heappop(heap)

    sum_value = one+two
    result += sum_value

    heapq.heappush(heap, sum_value)

print(result)
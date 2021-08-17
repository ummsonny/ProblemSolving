import sys

n = int(input())

arr = []
for i in range(n):
    arr.append(list(sys.stdin.readline().split()))

arr.sort(key = lambda x : (-int(x[1]),int(x[2]), -int(x[3]), x[0])) #이 줄이 메인!!! 1.https://ooyoung.tistory.com/59 : 문자열 정렬 2. https://dailyheumsi.tistory.com/67 : 오름차순 내림차순 조건!

for i in arr:
    print(i[0])
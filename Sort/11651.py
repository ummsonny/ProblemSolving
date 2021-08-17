import sys

n = int(input())

arr=[]
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

arr.sort(key = lambda x : (x[1], x[0]))
# arr.sort(key = lambda x : (x[1]))10,11줄처럼 하면 안된다!!!! 이건 y기준으로 한 결과에 x기준으로 정렬을 적용하라는 뜻
# arr.sort(key = lambda x : (x[0])) 즉, y가 같다면 x를 기준으로 정렬하라는 의미를 담으려면 9줄처럼 한번에 ㄱㄱㄱㄱ

for i in arr:
    print(i[0], i[1])

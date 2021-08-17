import sys
n = int(input())

arr = []
for i in range(n):
    arr.append(list(sys.stdin.readline().split()))#list(map(str, sys.stdin.readline().split())) 어차피 문자열로 받으니 map쓸 필요없다.

arr.sort(key = lambda x : int(x[0])) #여기 int(x[0])부분이 핵심 lambda는 '내가 출력으로 이걸 줄테니까 이거 가지고 정렬해!' 라는말

for i in arr:
    print(i[0],i[1])
import sys
n = int(sys.stdin.readline())

arr = [0]*10001
for i in range(n):
    arr[int(sys.stdin.readline())]+=1

for i in range(10001):
    if arr[i] !=0:
        for j in range(arr[i]):
            print(i)

# https://wikidocs.net/21057 append는 메모리 재할당을 하기 때문에 메모리를 효율적으로 쓰지 못한다.
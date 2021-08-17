import sys
a,b = map(int, sys.stdin.readline().split())

if b<10:#나머지가 무조건 10보다 작다.
    arr = []
    while a!=0:
        arr.append(str(a%b))
        a//=b
    print(''.join(reversed(arr)))
else:
    arr = []
    while a!=0:#나머지가 10보다 작거나 10이상이다.
        if a%b>=10:
            arr.append(chr(a%b+55))
        else:
            arr.append(str(a%b))
        a//=b
    print(''.join(reversed(arr)))

#미친 풀이
# system = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" #10진법이면 9 까지, 36진법이면 Z까지 표현된다
# N, B = map(int, input().split())
# answer = ''

# while N != 0:
#     answer += str(system[N % B]) #위치로 진법 변환, 문자열은 append말고 그냥 + 해도 된다.
#     N //= B
    
# print(answer[::-1]) reversed()대신 사용가능!!!!!!!!!!!!!!!!!!!!!!!!!!
#1. 나눠지는 경우
#2. 안나눠지는 경우 1. 음수, 2. 양수
import sys
n = int(sys.stdin.readline())
arr = ''
if n ==0: #n==0 일때 조건을 고려안하고 while만 돌리면 무한루프나와서 시간초과 그래서 꼭 해줘야해 
    sys.stdout.write('0')
else:#append()는 메모리를 재할당 하므로 메모리 초과 날 수 있으니 문자열은 + 써랏
    while n!=1:
        if n%(-2)==0:
            n //=(-2)
            arr = '0'+arr
        else:
            if n<0:
                n = n//(-2)+1
                arr = '1'+arr
            else:
                n = n//(-2)+1
                arr = '1'+arr

    arr = '1'+arr

    sys.stdout.write(arr)
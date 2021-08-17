#https://conak-diary.tistory.com/7 : EOF해결 두가지 방법
#1000000까지 소수를 미리 구해놓는 풀이도 있는데 나는 그러지 않았다. 굳이?
import sys,math

#소수 판별 
def is_prime_number(x):
    for i in range(2,int(math.sqrt(x))+1): #2부터 제곱근까지 나누어 지면 소수아님
        if x%i==0:
            return False
    return True

for line in sys.stdin:
    n = int(line)
    if n==0: break
    for i in range(3,(n//2)+1,2): #2는 짝수이므로 고려대상 아님
        if is_prime_number(i) and is_prime_number(n-i):
            print("{} = {} + {}".format(n, i, n-i))
            break
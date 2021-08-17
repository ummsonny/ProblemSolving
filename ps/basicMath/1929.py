import math
#소수판별은 특정 수의 제곱근 까지만 해보면 된다.
def is_prime_number(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i ==0:
            return False;
    return True

a,b = map(int, input().split())

for i in range(a,b+1):
    if is_prime_number(i) and i!=1:
        print(i)

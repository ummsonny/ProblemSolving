def is_prime_number(x):
    for i in range(2,x):
        if x%i ==0:
            return False;
    return True

n = int(input())
data = list(map(int, input().split()))
ans_cnt=0

for i in range(n):
    if is_prime_number(data[i]) and data[i]!=1:
        ans_cnt+=1

print(ans_cnt)
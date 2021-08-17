from collections import defaultdict
n = int(input())
dic = defaultdict(int)

d = 2


while n>1:
    if(n%d==0):
        dic[d]+=1
        n//=d
    else:
        d+=1

for i in dic.keys():
    for j in range(dic[i]):
        print(i)

#그냥 내가 소인수분해하는 것처럼 하면된다. 작은 수 부터 안 나누어 질때까지 나누고 그다음 다음 수로 계속 나누고 ....ex) 2로 계속 나누고 안나눠지면 3으로 계속나누고....
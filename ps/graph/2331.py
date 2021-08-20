n,a = map(int, input().split())

ans = [n]

while True:
    s=0
    while n>0:# 각 자리수 거듭제곱 후 더하기 연산
        s+=((n%10)**a)
        n//=10

    #리스트에 있는지 없는지 찾기
    if s in ans:
        find = ans.index(s)
        break;
    else:
        ans.append(s)
        n=s

print(find)
A,B = map(int, input().split())
l = int(input())
arr = list(map(int, input().split()))

ans1 = 0
for i in range(l-1, -1, -1):
    ans1=ans1+arr[i]*pow(A,l-1-i)

ans2=''
while ans1!=0:
    ans2=' '+str(ans1%B)+ans2
    ans1//=B

print(ans2.lstrip())
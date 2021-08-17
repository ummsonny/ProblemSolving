str = input()
n=len(str)

count=0
sum=0

for i in range(n):
    if str[i] == '(':
        sum += 1
    elif str[i] == ')':
        if str[i-1]=='(':
            sum-=1
            count+=sum
        elif str[i-1]==')':
            sum-=1
            count+=1

print(count)

# '(' 나오면 그냥 스택에 추가!
# ')' 나오면 2갈래로 나뉜다.
    #1. 앞에 '(' 일 경우 : pop하고 스택에 남은 애들 갯수를 count에 더해준다.
    #2. 앞에 ')' 일 경우 : pop하고 1을 count에 더해준다. 
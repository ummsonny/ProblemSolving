n = list(input())

for i in range(len(n)):
    if n[i].isupper():
        #n[i]=chr(ord(n[i])+13)이렇게 String은 각각의 문자를 고칠 수 없다. 그래서 list로 변환해주어야 한다.(1번줄에서 list로 변환)
        if ord(n[i])+13>90:
            n[i]=chr((ord(n[i])-13))#더 깔끔한 풀이
            #n[i]=chr(64+(ord(n[i])+13)%90)
        else:
            n[i]=chr(ord(n[i])+13)
    elif  n[i].islower():
        if ord(n[i])+13>122:
            n[i]=chr((ord(n[i])-13)) #더 깔끔한 풀이
            #n[i]=chr(96+(ord(n[i])+13)%122)
        else:
            n[i]=chr(ord(n[i])+13)

for i in n:
    print(i,end="")
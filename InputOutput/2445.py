n = int(input())

#내 풀이
#https://codechacha.com/ko/python-reverse-string/ 문자열 뒤집는 방법
#1번이 내풀이 --> 슬라이싱이용
#2번이 reversed풀이
for i in range(1,n+1):
    str = "*"*i+" "*(n-i)
    print(str+str[::-1])#1번
for i in range(n-1,0,-1):
    str = "*"*i+" "*(n-i)
    print(str+"".join(reversed(str)))#2번

#다른 풀이 이건 그냥 규칙 찾아서 조진것이다.
# n = int(input())
# for i in range(1, n):
#     print('*'*i + ' '*2*(n-i) + '*'*i)
# for i in range(n, 0, -1):
#     print('*'*i + ' '*2*(n-i) + '*'*i)
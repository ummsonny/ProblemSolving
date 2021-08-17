#내 풀이
num = int(input())
number = int(input())
#print(list(map(int, input())))
sum=0

for i in range(num):
    sum+=number%10
    number //= 10
print(sum)


#https://ooyoung.tistory.com/67
#3가지 방법이 더 있다.
#첫 번째 방법에서 문자열은 문자들의 list임을 기억하자(map함수 https://velog.io/@suasue/Python-map-%ED%95%A8%EC%88%98)
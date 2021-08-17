# from collections import defaultdict
# import math
# dic = defaultdict(int)
# n = int(input())
# #일단 팩토리얼 구해
# sum=1
# for i in range(1,n+1):
#     sum*=i
# n=sum
# #소인수 분해해서 2,5 개수 구해
# d = 2
# if n==0 or n==1:
#     print('0')
# else:
#     while n>1 and d<6:
#         if n%d==0:
#             dic[d]+=1
#             n//=d
#         else:
#             d+=1

#     if (2 in dic.keys()) and (5 in dic.keys()):
#         print(dic[5] if dic[5]<=dic[2] else dic[2])
#     else:
#         print('0')
#위에꺼는 개 허접한 내풀이
#밑에꺼는 개쩌는 풀이
n = int(input())
print(n//5+n//25+n//125)
#1~n까지 일렬로 늘여놓고 거기서 5의 개수를 찾으면 된다. 2는 상관 없다 어차피 5개수보다 훨씬 많기 때문
#n//5로 일단 한번뽑고 n//25로 남은 5개수 뽑고 n//125로 나머지 5개수 다 뽑아 
#조건에 1<=n<=500이기 때문에 625는 고려하지 않는다. 
import sys

while True:
    ans = [0]*4
    n = sys.stdin.readline()[:-1] #마지막의 '\n'없애줘야지 / 22줄처럼해줘도 된다.

    if not n: #EOF처리
        break;
    for i in n:
        if i.islower():
            ans[0]+=1
        elif i.isupper():
            ans[1]+=1
        elif i==' ':#isspace()도 됨
            ans[3]+=1
        else:# isdigit()도 됨
            ans[2]+=1
    print(ans[0], ans[1], ans[2], ans[3])#35줄처럼도 가능

# import sys 
# while True: 
#     line = sys.stdin.readline().rstrip('\n') 
#     up, lo, sp, nu = 0, 0, 0, 0 
#     if not line: 
#         break 
#     for l in line: 
#         if l.isupper(): 
#             up += 1 
#         elif l.islower(): 
#                 lo += 1 
#         elif l.isdigit(): 
#             nu += 1 
#         elif l.isspace(): 
#             sp += 1 
#     sys.stdout.write("{} {} {} {}\n".format(lo, up, nu, sp))

# 문제에서는 몇 개의 테스트 케이스가 주어진다고 정해지지 않았기 때문에 EOF 검사를 해줘야 한다. 
# 방법1 sys.stdin.readline()으로는 입력이 있었는지 None인지 확인하면 될 것이다.
# 방법2 이와 다르게 input()을 사용했다면, try ~ except 문으로 EOFError를 처리해주면 될 것이다.


    

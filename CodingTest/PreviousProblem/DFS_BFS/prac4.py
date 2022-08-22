def balanced_index(p): # 균형잡힌 문자열의 인덱스 반환
    count = 0 #왼쪽 괄호의 개수
    for i in range(len(p)):
        if p[i] == '(':
            count +=1
        else:
            count -=1

        if count == 0:
            return i

def check_proper(p): # 올바른 문자열
    count = 0 # 왼쪽 괄호의 개수
    for i in p:
        if i == '(':
            count +=1
        else:
            if count == 0: # 남는 '('가 없자나 그래서 짝을 못 지음
                return False
            count -=1
    return True

def solution(p): #균잡 -> 올바른 으로 바꾸는 함수임을 기억!
    answer = "" # return 할 값

    if p== "":
        return answer

    index = balanced_index(p)
    u = p[:index+1]
    v = p[index+1:]

    if check_proper(u):
        answer = u+solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1]) # 밑에 for문 돌리려고 list로 변환
        for i in range(len(u)):
            if u[i]=='(':
                u[i]=')'
            else:
                u[i]='('

        answer += "".join(u)
    
    return answer

print(solution("()))((()"))

# 내 풀이
input_str = input()


def first(input_str): # 균형잡힌 문자열 반환
    count=0
    for i in range(len(input_str)):
        if input_str[i]=="(":
            count+=1
        else:
            count-=1

        if count==0:
            return i

def second(input_str):
    count=0
    for i in range(len(input_str)):
        if input_str[i]=="(":
            count+=1
        else:
            if count == 0:
                return False
            count-=1
    return True

def solution(input_str):

    if input_str=="":
        return ""

    answer = ""
    proper = first(input_str)
    if second(input_str[:proper+1]):
        answer = input_str[:proper+1]+solution(input_str[proper+1:])
    else:
        answer+="("
        answer+=solution(input_str[proper+1:])
        answer+=")"
        answer+="".join(list(map(lambda x : ")" if x=="(" else "(",input_str[1:proper])))
    
    return answer

print(solution(input_str))
    
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
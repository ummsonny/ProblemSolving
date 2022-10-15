def solution(today, terms, privacies):

    term = {}
    for arr in terms:
        a,b = arr.split()
        term[a]=int(b)
    answer = []

    length = len(privacies)
    todaytemp = list(map(int, today.split('.')))

    for i in range(length):
        date, t = privacies[i].split()
        date = list(map(int, date.split('.')))
        t = term[t] # 100달까지 있음
        a,t = t//12, t%12
        y,m,d = int(date[0]),int(date[1]),int(date[2])
        if m+t>12:
            y+=(a+1)
            m=(m+t)-12
        else:
            y+=(a)
            m=m+t
        if d==1:
            if m==1:
                y-=1
                m=12
                d=28
            else:
                m-=1
                d=28
        else:
            d-=1
        date = [y,m,d]
        #비교
        if date[0]<todaytemp[0]:
            answer.append(i+1)
        elif date[0]==todaytemp[0]:
            if date[1]<todaytemp[1]:
                answer.append(i+1)
            elif date[1]==todaytemp[1]:
                if date[2]<todaytemp[2]:
                    answer.append(i+1)

    return answer

today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
# today = "2020.01.01"
# terms = ["Z 3", "D 5"]
# privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
print(solution(today,terms, privacies))
# 완전 탐색
from itertools import product

def solution(users, emoticons):
    length = len(emoticons) #이모티콘 개수

    sale = [10, 20, 30, 40]
    global_service_cnt = 0
    global_emotion_sale = 0

    for candi in product(sale, repeat = length):
        # print(candi)
        service_cnt = 0
        emoticon_sale = 0

        for spercent,svalue in users: # 각 기준 퍼센트 및 가격
            wallet = 0
            for i in range(length):

                if candi[i]>=spercent:
                    # print(int(((100-candi[i])/100)*emoticons[i]))
                    wallet+=(int((100-candi[i])*emoticons[i]/100))

            if wallet>=svalue: #내 기준보다 비싸!
                service_cnt +=1
            else:
                emoticon_sale+=wallet
        # print(service_cnt,emoticon_sale)
        # print(service_cnt,emoticon_sale)

        if global_service_cnt<service_cnt:
            global_service_cnt = service_cnt
            global_emotion_sale = emoticon_sale
        elif global_service_cnt==service_cnt:
            if global_emotion_sale<emoticon_sale:
                global_service_cnt = service_cnt
                global_emotion_sale = emoticon_sale

    answer = [global_service_cnt,global_emotion_sale]
    return answer

# print(solution([[40,10000],[25,10000]],[7000,9000]))
print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]],[1300, 1500, 1600, 4900]))

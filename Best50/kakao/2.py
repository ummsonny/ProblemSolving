def solution(cap, n, deliveries, pickups):

    answer = int(1e9)
    dist = 0

    while not(deliveries[0]==0 and pickups[0]==0):

        cap_temp = cap
        #배달
        for i in range(dedistidx,-1,-1):
            if 0<deliveries[i]<=cap_temp:
                cap_temp, deliveries[i] = cap_temp-deliveries[i], 0
                dedistidx = max(dedistidx,i)
            if cap_temp<=0:
                print(deliveries, cap_temp)
                break

        cap_temp = cap
        #수거
        for i in range(pidistidx,-1,-1):
            if 0<pickups[i]<=cap_temp:
                cap_temp, pickups[i] = cap_temp-pickups[i],0
                pidistidx = max(pidistidx,i)
            if cap_temp<=0:
                print(pickups, cap_temp,i)
                break

        print(deliveries, pickups)
        print(dedistidx, pidistidx)
        dist += (max(dedistidx, pidistidx) + 1)
        answer = dist*2
        print('k')

    return answer

# print(solution(4,5,[1,0,3,1,2],[0,3,0,4,0]))
print(solution(2,7,[1,0,2,0,1,0,2],[0,2,0,1,0,2,0]))
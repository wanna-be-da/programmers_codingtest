money = [1,2,3,1,4,4]

def solution(money):

    length = len(money)
    #2번 index부터 length-2번 index까지 채우기
    sol1 = [0] * length
    sol1[length-2] = money[length-2]
    sol1[length-3] = max(money[length-2], money[length-3])
    for i in range(length-4, 1, -1):
        sol1[i] = max(money[i] + sol1[i+2], sol1[i+1])

    #1번 index부터 length-1번 index까지 채우기
    sol2 = [0] * length
    sol2[length-1] = money[length-1]
    sol2[length-2] = max(money[length-1], money[length-2])
    for i in range(length-3, 0, -1):
        sol2[i] = max(money[i] + sol2[i+2], sol2[i+1])

    return max(money[0] + sol1[2], sol2[1])

print(solution(money))
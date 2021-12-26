def solution(n, times):
    answer = 0

    # times를 정렬
    times.sort()

    # [심사시간, 맡은시간]의 행렬 세팅
    sol = [[times[0], n * times[0]]]
    for time in times[1:]:
        sol.append([time, 0])
    max = n * times[0]
    max_index = 0

    # while문 돌려가며 개선
    while True:
        changed = False
        for i in range(len(times)):
            if i != max_index and sol[i][0] + sol[i][1] < max:  # 이렇게 찾지 말고 이진탐색을 해야함
                if max - sol[max_index][0] >= sol[i][0] + sol[i][1]:
                    max -= sol[max_index][0]
                    sol[i][1] += sol[i][0]
                else:
                    sol[i][1] += sol[i][1]
                    max = sol[i][1]
                    sol[max_index][1] -= sol[max_index][0]
                    max_index = i
                changed = True
                break
        if not changed:
            break

    return max
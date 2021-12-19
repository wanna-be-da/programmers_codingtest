def solution(progresses, speeds):
    answer = []
    remaining_time = [None] * len(progresses)
    for i in range(len(progresses)):
        remaining_time[i] = (100 - progresses[i]) // speeds[i]
        if (100 - progresses[i]) % speeds[i] != 0:
            remaining_time[i] += 1

    pointer = 0
    cnt = 1
    bottleneck = remaining_time[0]
    while True:
        if remaining_time[pointer+1] <= bottleneck:
            pointer += 1
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            pointer += 1
            bottleneck = remaining_time[pointer]

        if pointer == len(progresses) - 1:
            answer.append(cnt)
            return answer

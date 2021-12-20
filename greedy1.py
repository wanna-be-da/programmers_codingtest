def solution(n, lost, reserve):
    answer = 0

    students = [1] * n
    for l in lost:
        students[l - 1] -= 1
    for r in reserve:
        students[r - 1] += 1

    if students[0] == 2:
        if students[1] == 0:
            students[0] -= 1
            students[1] += 1

    for s in range(1, len(students) - 1):
        if students[s] == 2:
            if students[s - 1] == 0:
                students[s - 1] += 1
                students[s] -= 1
            elif students[s + 1] == 0:
                students[s] -= 1
                students[s + 1] += 1

    if students[-1] == 2:
        if students[-2] == 0:
            students[-1] -= 1
            students[-2] += 1

    for s in students:
        if s >= 1:
            answer += 1

    return answer
def solution(priorities, location):
    answer = 0
    max_ = max(priorities)

    #큐의 첫번째 원소를 꺼내고 이것이 max인지 확인, 아니라면 큐에 다시 추가, 맞다면 출력 횟수 1증가
    #꺼낸다면 location은 1이 줄고
    #location이 꺼내는 차례일 때는 특별처리

    while True:
        if location == 0:
            temp = priorities.pop(0)
            if temp == max_:
                return answer + 1
            else:
                priorities.append(temp)
                location = len(priorities) - 1


        temp = priorities.pop(0)
        if temp == max_:
            answer += 1
            max_ = max(priorities)
            location -= 1
        else:
            priorities.append(temp)
            location -= 1


def solution(citations):
    answer = 0
    length = len(citations)
    citations.sort()
    temp = 0
    point = 0
    while True:
        for index in range(point, len(citations)):
            if citations[index] < temp:
                point += 1
            else:
                break

        if length - point >= temp:
            temp += 1
        else:
            return temp - 1
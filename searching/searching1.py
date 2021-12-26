def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5] * 8
    two = [2, 1, 2, 3, 2, 4, 2, 5] * 5
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 4

    cnt1, cnt2, cnt3 = 0, 0, 0
    for i in range(len(answers)):
        try:
            if answers[i] == one[i]:
                cnt1 += 1
            if answers[i] == two[i]:
                cnt2 += 1
            if answers[i] == three[i]:
                cnt3 += 1
        except:
            one.extend(one)
            two.extend(two)
            three.extend(three)
            if answers[i] == one[i]:
                cnt1 += 1
            if answers[i] == two[i]:
                cnt2 += 1
            if answers[i] == three[i]:
                cnt3 += 1

    cnt = [cnt1, cnt2, cnt3]
    max_ = max(cnt)
    for k, v in enumerate(cnt):
        if v == max_:
            answer.append(k + 1)

    return answer
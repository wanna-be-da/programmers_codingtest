def solution(clothes):
    closet = {}
    for c in clothes:
        try:
            closet[c[1]].append(c[0])
        except:
            closet[c[1]] = [c[0]]

    if len(closet) == 1:
        for v in closet.values():
            return len(v)

    else:
        answer = 1
        for v in closet.values():
            answer *= len(v) + 1
        return answer - 1
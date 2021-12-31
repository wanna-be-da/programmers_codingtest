brown = 24
yellow = 24

def solution(brown, yellow):

    #brown : 2a + 2b + 4
    #yellow : ab
    #answer : [b+2, a+2]

    for a in range(1, brown//4):
        if a * (brown//2 - a - 2) == yellow:
            return [brown//2 - a, a+2]

print(solution(brown, yellow))
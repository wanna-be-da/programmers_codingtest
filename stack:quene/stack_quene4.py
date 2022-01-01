prices = [1,2,3,2,3]

def solution(prices):
    answer = [0] * len(prices)

    #prices 항목을 돌면서 시간, value를 기록, 더 작은 것이 나왔을 때 마다 모두 pop
    #값이 변하는 위치를 기록 하면서 그 전까지 모두 자르는게 나을 것 같은데

    stack = [[prices[0], 0]]
    for t in range(1, len(prices)):
        #t는 시간
        while True:
            if stack: # 스택이 있고
                if stack[-1][0] <= prices[t]:
                    stack.append([prices[t], t])
                    break
                else:
                    out = stack.pop()
                    answer[out[1]] = t - out[1]
            else:
                stack.append([prices[t], t])
                break

    for s in stack:
        answer[s[1]] = len(prices) - s[1] - 1

    return answer

print(solution(prices))
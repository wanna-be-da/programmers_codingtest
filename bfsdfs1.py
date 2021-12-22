def solution(numbers, target):
    return DFS(numbers, target)


def DFS(numbers, target):
    if len(numbers) == 1:
        if numbers[0] == abs(target):
            return 1
        else:
            return 0
    else:
        return DFS(numbers[1:], target + numbers[0]) + DFS(numbers[1:], target - numbers[0])
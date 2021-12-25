def solution(number, k):
    del_index = 1
    while k > 0:
        for i in range(max(0, del_index - 1), len(number) - 1):
            if number[i] < number[i + 1]:
                number = number[:i] + number[i + 1:]
                del_index = i
                k -= 1
                break
            if i == len(number) - 2:
                return number[:-k]


    return number

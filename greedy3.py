def solution(number, k):
    while k > 0:
        del_number = number[0]
        del_index = 0
        for i in range(1, len(number)):
            if number[i] > del_number:
                break
            del_number = number[i]
            del_index = i

        number = number[:del_index] + number[del_index + 1:]
        k -= 1

    return number
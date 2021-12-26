def solution(numbers):
    answer = ''
    startwith = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
    for number in numbers:
        startwith[int(str(number)[0])].append(number)

    for i in range(9, -1, -1):
        startwith[i] = sort_numbers(startwith[i])
        for number in startwith[i]:
            answer += str(number)

    return answer


def is_big(a, b):
    ab = str(a) + str(b)
    ba = str(b) + str(a)
    if int(ab) >= int(ba):
        return True
    else:
        return False


def sort_numbers(num_list):
    for i in range(len(num_list)):
        for j in range(i + 1, len(num_list)):
            if not is_big(num_list[i], num_list[j]):
                num_list[i], num_list[j] = num_list[j], num_list[i]
    return num_list
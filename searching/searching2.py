from itertools import permutations
numbers = '17'


def solution(numbers):
    answer = 0
    numbers = list(numbers)
    candidates = gen_candidate(numbers)
    for candidate in candidates:
        if is_prime(candidate):
            answer += 1
    return answer

def gen_candidate(numbers):
    candidate = []
    for length in range(1, len(numbers)+1):
        permutation = permutations(numbers, length)
        for element in permutation:
            str = ''
            for num in element:
                str += num
            candidate.append(int(str))
    return set(candidate)

def is_prime(candidate):
    if candidate == 1 or candidate == 0:
        return False

    for i in range(2, int(candidate ** 0.5 + 1)):
        if candidate % i == 0:
            return False

    return True

print(solution(numbers))



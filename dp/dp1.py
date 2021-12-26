def solution(N, number):
    table = [[], [], [], [], [], [], [], [], []]
    for i in range(1, 9):
        table[i].append(int(str(N) * i))
        if number in table[i]:
            return i
        for j in range(1, i // 2 + 1):
            for m in table[j]:
                for n in table[i - j]:
                    gen = gen_numbers(m, n)
                    if number in gen:
                        return i
                    table[i].extend(gen)
        table[i] = list(set(table[i]))
    return -1


def gen_numbers(a, b):
    if a != 0 and b != 0:
        return [a * b, a + b, a - b, b - a, a // b, b // a]
    elif a != 0:
        return [-a]
    elif b != 0:
        return [-b]
    else:
        return []
puddles = []

def solution(m, n, puddles):
    map = [[1] * (m+1) for _ in range(n+1)]

    for puddle in puddles:
        map[puddle[1]][puddle[0]] = 0

    for i in range(2, n+1):
        if map[i][1] == 0:
            for j in range(i+1, n+1):
                map[j][1] = 0
            break

    for j in range(2, m+1):
        if map[1][j] == 0:
            for i in range(j+1, m+1):
                map[1][i] = 0
            break

    for j in range(2, m+1):
        for i in range(2, n+1):
            if map[i][j] != 0:
                map[i][j] = (map[i-1][j] + map[i][j-1]) % 1000000007

    return map[n][m]

print(solution(5, 5, puddles))
N = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

def solution(n, edge):
    answer = 0

    #행렬만들기 n+1 * n+1 행렬 만들기
    graph = [[0]*(n+1) for _ in range(n+1)]
    for e in edge:
        graph[e[0]][e[1]] = 1
        graph[e[1]][e[0]] = 1

    #1번노드로부터 큐를 활용한 DFS시작
    visited = [0] * (n+1)
    visited[1] = 1
    quene = [1]
    while len(quene) > 0:
        temp = quene.pop(0)
        adjacents = []
        for index, val in enumerate(graph[temp]):
            if val == 1 and visited[index] == 0:
                adjacents.append(index)
                visited[index] = visited[temp] + 1
        quene.extend(adjacents)

    max_ = max(visited)
    for n in visited:
        if n == max_:
            answer += 1

    return answer

print(solution(N, edge))
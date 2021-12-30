n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

def solution(n, computers):
    answer = 0

    visited = [0] * n

    while True:
        # 한번의 시행, 한번의 DFS 종료
        answer += 1

        start = -1
        # 시작 노드 찾기
        for i in range(len(visited)):
            if visited[i] == 0:
                start = i

        if start == -1:
            answer -= 1
            break

        # start 노드에서 BFS, 큐를 활용한
        quene = [start]
        while len(quene) > 0:
            tmp = quene.pop(0)
            visited[tmp] = 1
            for node in range(len(computers[tmp])):
                if computers[tmp][node] == 1 and visited[node] == 0:
                    visited[node] += 1
                    quene.append(node)

    return answer

print(solution(n, computers))
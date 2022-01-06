begin = 'hit'
target = 'cog'
words = ["hot", "dot", "dog", "lot", "log", 'cog']

def solution(begin, target, words):
    #target: 0 ~ len-3 index, begin: len -2 index, target: len-1 index
    #begin에서 target 까지 몇번의 dfs로 가능한가
    if target not in words:
        return 0
    else:
        words.remove(target)

    words.append(begin)
    words.append(target)

    length = len(words)
    graph = [[0] * len(words) for _ in range(length)]

    for i in range(length):
        for j in range(i+1, length):
            if adjacent(words[i], words[j]):
                graph[i][j] = 1
                graph[j][i] = 1

    # len-2 node에서 len-1 node까지 몇칸인지 bfs로 찾기
    queue = [length-2]
    visited = [0] * length
    visited[length-2] = 1
    while queue:
        temp = queue.pop(0)
        for i in range(length):
            if graph[temp][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = visited[temp] + 1
                if i == length -1:
                    visited[length-1] -= 1
                    break
    return visited[length-1]

def adjacent(word1, word2):
    word_length = len(word1)
    cnt = 0
    for i in range(word_length):
        if word1[i] == word2[i]:
            cnt += 1

    if cnt == word_length - 1:
        return True
    else:
        return False

print(solution(begin, target, words))
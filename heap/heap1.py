import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0

    while True:
        first = heapq.heappop(scoville)

        if first >= K:
            return cnt
        try:
            second = heapq.heappop(scoville)
        except:
            return -1
        new = first + second * 2
        cnt += 1
        heapq.heappush(scoville, new)

print(solution(scoville, K))
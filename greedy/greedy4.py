def solution(people, limit):
    people.sort()
    capacity = [limit]

    for person in people:
        for i in range(len(capacity)):
            if person <= capacity[i]:
                capacity[i] -= person
                capacity = insertion_sort(capacity, i)
                break
            if i == len(capacity)-1:
                capacity.append(limit - person)
                capacity = insertion_sort(capacity, i+1)

    return len(capacity)

def insertion_sort(list, index):
    if len(list) == 1:
        return list
    item = list.pop(index)
    for i in range(len(list)):
        if item <= list[i]:
            list.insert(i, item)
            break
        if i == len(list) -1:
            list.append(item)
    return list

#3명 넘게 타도 되는줄..

def solution(people, limit):
    people.sort()
    answer = 0
    p1 = 0
    p2 = len(people) -1

    while p1 <= p2:
        if people[p1] + people[p2] <= limit:
            p1 += 1
            p2 -= 1
        else:
            p2 -= 1
        answer += 1
    return answer
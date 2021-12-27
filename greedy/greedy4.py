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




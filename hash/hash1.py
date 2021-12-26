def solution(participant, completion):
    part_dict = {}
    for p in participant:
        try:
            part_dict[p] += 1
        except:
            part_dict[p] = 1

    for c in completion:
        part_dict[c] -= 1

    for k, v in part_dict.items():
        if v != 0:
            return k
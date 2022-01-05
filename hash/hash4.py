genres = ["classic", "pop", "classic", "classic", "pop", 'k']
plays = [500, 2500, 150, 800, 2500, 10000]

def solution(genres, plays):
    answer = []

    song_dict = {}
    song_sum = {}

    for song_number, genre in enumerate(genres):
        try:
            song_dict[genre].append([song_number, plays[song_number]])
            song_sum[genre] += plays[song_number]
        except:
            song_dict[genre] = [[song_number, plays[song_number]]]
            song_sum[genre] = plays[song_number]

    for genre in sorted(song_sum.items(), key=lambda x: x[1], reverse=True):
        genre = song_dict[genre[0]]
        if len(genre) == 1:
            answer.append(genre[0][0])
        else:
            genre.sort(key=lambda x: x[1])
            top1 = genre.pop()
            top2 = genre.pop()
            if top1[1] == top2[1]:
                temp = [top1[0], top2[0]]
                temp.sort()
                answer.extend(temp)
            else:
                answer.append(top1[0])
                answer.append(top2[0])
    return answer

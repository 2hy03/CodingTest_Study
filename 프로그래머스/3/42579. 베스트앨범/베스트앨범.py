def solution(genres, plays):
    answer = []
    play_dic={}     #각 노래 연결,genres : (plays,고유번호)
    play_sum={}     #장르별 재생 합, genres : sum(play)
    

    for i in range(len(genres)):
        play_dic[genres[i]]= play_dic.get(genres[i], []) + [(plays[i],i)]
        play_sum[genres[i]]=play_sum.get(genres[i],0) + plays[i]
    
     # 장르별 재생 합(play_sum)을 재생 횟수 기준으로 내림차순 정렬
    sorted_play_sum = sorted(play_sum.items(), key=lambda x: x[1], reverse=True)

    # 각 장르에서 가장 많이 재생된 두 곡 선택
    for genre, _ in sorted_play_sum:
        # 장르별로 재생 횟수 기준으로 노래 정렬
        sorted_songs = sorted(play_dic[genre], key=lambda x: (-x[0], x[1]))

        # 상위 두 곡을 answer에 추가 (고유번호 기준)
        answer.extend([song[1] for song in sorted_songs[:2]])

    return answer

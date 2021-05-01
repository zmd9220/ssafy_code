import json
from pprint import pprint


def movie_info(movies, genres):
    # 여기에 코드를 작성합니다.  
    # 전체 movies 딕셔너리에서 각 요소별로 해당 하는 정보만 얻어와서 집어넣기
    result = [] # 딕셔너리를 넣을 리스트
    for movie in movies:
        # 전체 movie.json에서 기본으로 가져올 아이템들 가져오기
        item = {'genre_names': [], 'id': movie.get('id'),
        'overview': movie.get('overview'), 'poster_path': movie.get('poster_path'),
        'title': movie.get('title'), 'vote_average': movie.get('vote_average')
        } # 각 영화별 정보
        
        # 장르 코드를 가져오기
        gcode = movie.get('genre_ids')
        

        # 각 장르 코드 마다
        for code in gcode:
            # 해당 장르 코드 리스트를 순회하며 id가 같은지 확인 
            for genre in genres:
                # 같은 아이디를 찾음(해당 코드임) = result 장르탭에 삽입
                if code == genre.get('id'):                    
                    item['genre_names'].append(genre.get('name'))
                    break # 더 돌 필요가 없으므로 끝내기
        result.append(item)

    return result  
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
import json
from pprint import pprint


def movie_info(movie, genres):
    # 여기에 코드를 작성합니다.  
    # 전체 movie.json에서 기본으로 가져올 아이템들 가져오기
    result = {'genre_names': [], 'id': movie.get('id'),
    'overview': movie.get('overview'), 'poster_path': movie.get('poster_path'),
    'title': movie.get('title'), 'vote_average': movie.get('vote_average')
    }
    
    # 장르 코드를 가져오기
    gcode = movie.get('genre_ids')
    # print(gcode) # 확인용

    # 각 장르 코드 마다
    for code in gcode:
        # 해당 장르 코드 리스트를 순회하며 id가 같은지 확인 
        for genre in genres:
            # 같은 아이디를 찾음(해당 코드임) = result 장르탭에 삽입
            if code == genre.get('id'):
                # print(genre.get('name')) # 확인용
                result['genre_names'].append(genre.get('name'))
                break # 더 돌 필요가 없으므로 끝내기
    
    return result


        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
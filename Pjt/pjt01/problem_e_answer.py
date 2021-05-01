import json


def dec_movies(movies):
    result = [] # 제목 리스트를 반환할 리스트

    # 모든 영화를 순회해야함
    for movie in movies:
        # 파일 접근을 위해 알아낼 요소는 id
        movie_id = str(movie.get('id'))
        # 해당 id에 맞는 파일 읽기
        movie_json = open('data/movies/'+movie_id+'.json', encoding='UTF8')
        movie_list = json.load(movie_json)

        # 개봉일자 정보 가져오기
        release_date = movie_list.get('release_date')
        # 문자열 슬라이싱 하기 - 월 부분만 
        release_date = release_date[5:7]
        

        # 해당 개봉 월이 12월 이면 영화 제목을 리스트에 넣기
        if int(release_date) == 12:
            # print(movie.get('title'), release_date) # 확인용
            result.append(movie.get('title'))
    
    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
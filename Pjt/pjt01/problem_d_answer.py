import json


def max_revenue(movies):
    
    max_movie = '' # 수익 높은 영화 제목
    max_value = 0 # 수익 비교용
    # 모든 무비를 순회 하며 수익을 비교해야함
    for movie in movies:
        # 수익을 알아내기 위한 키워드는 파일 접근을 위해 알아낼 요소는 id
        movie_id = str(movie.get('id'))
        # 해당 id에 맞는 파일 읽기
        revenue_json = open('data/movies/'+movie_id+'.json', encoding='UTF8')
        revenue_list = json.load(revenue_json)
        
        # 비교 위한 값 생성
        now_value = int(revenue_list.get('revenue'))
        if max_value < now_value : # 수익이 더 클 경우 교체
            max_value = now_value
            max_movie = movie.get('title')
    
    return max_movie

 
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
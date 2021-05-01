import requests
from tmdb import URLMaker
from pprint import pprint


def recommendation(title):
    # 결과값을 담을 result 리스트
    result = []
    # URLMaker 클래스를 통해 maker 인스턴스 생성
    maker = URLMaker('031b6156fbe52ee9595fddf7b81190fa')
    # 영화 제목을 토대로 movie_id 메소드를 사용하여 해당 영화의 id를 찾아 내기
    title_id = maker.movie_id(title)
    # 올바르지 않은 영화 제목을 검색할 경우 title_id에 None이 반환되므로 
    # title_id = None이라는 뜻은 잘못된 영화 제목 검색으로 인해 id가 없을 때
    if title_id == None:
        # 3번 조건 - id 가 없을 때 None 반환
        return None

    # 여기서 부터는 id를 찾아 냈을 때의 경우
    # url를 만들기 위해 get_url에 인자를 넣어 url 문자열 생성하려고 했으나, 양식이 미묘하게 다르므로 별도 생성
    recommend_url = f'https://api.themoviedb.org/3/movie/{title_id}/recommendations?api_key=031b6156fbe52ee9595fddf7b81190fa&language=ko'
    # 해당 문자열을 토대로 requests.get을 통해 해당 url 페이지의 정보를 가져옴(res로)
    res = requests.get(recommend_url) 
    # 가져온 정보(json)를 딕셔너리로 변환
    recommend_movies = res.json()
    # 해당 영화 정보들을 순회(위치는 results)하며 영화 제목을 리스트에 넣기
    # 4번 조건 - 추천 영화가 없으면 result는 빈 리스트이므로 빈 리스트 그대로 반환 될 것(순회를 안하므로)
    for movie in recommend_movies['results']:
        result.append(movie['title'])
    # 모든 작업 종료 후 결과 리스트 반환
    return result


if __name__ == '__main__':
    # 제목 기반 영화 추천
    pprint(recommendation('기생충'))
    # =>   
    # ['원스 어폰 어 타임 인… 할리우드', '조조 래빗', '결혼 이야기', '나이브스 아웃', '1917', 
    # '조커', '아이리시맨', '미드소마', '라이트하우스', '그린 북', 
    # '언컷 젬스', '어스', '더 플랫폼', '블랙클랜스맨', '포드 V 페라리', 
    # '더 페이버릿: 여왕의 여자', '두 교황', '작은 아씨들', '테넷', '브레이킹 배드 무비: 엘 카미노']
    pprint(recommendation('그래비티'))    
    # => []
    pprint(recommendation('id없는 영화'))
    # => None

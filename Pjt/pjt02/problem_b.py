import requests
from tmdb import URLMaker
from pprint import pprint


def vote_average_movies():
    # 결과값을 담을 result 리스트
    result = []
    # URLMaker 클래스를 통해 maker 인스턴스 생성
    maker = URLMaker('031b6156fbe52ee9595fddf7b81190fa')
    # url를 만들기 위해 get_url에 인자를 넣어 url 문자열 생성
    url = maker.get_url(region='KR', language='ko')
    # 해당 문자열을 토대로 requests.get을 통해 해당 url 페이지의 정보를 가져옴(res로)
    res = requests.get(url) 
    # 가져온 정보(json)를 딕셔너리로 변환
    popular_movies = res.json()


    # 페이지를 보니 평점은 results 딕셔너리 내부의 vote_average 라는 키를 통해 접근 할 수 있다.
    # 그리고 각 영화들 마다 평점을 확인 해야 하므로 for문을 통해 순회
    # 정리 하자면 results라는 영화정보가 담긴 딕셔너리를 데이터로 담고 있는 리스트에서 하나씩 순회
    # results(리스트) - 각 영화 정보(results의 아이템이면서 각각 딕셔너리로 구성)
    for movie in popular_movies['results']: 
        # 만약 해당 영화의 평점이 8점 이상이라면
        if movie['vote_average'] >= 8:
            # 해당 영화 제목(title)을 결과 리스트에 넣기
            result.append(movie['title'])

    # 모든 작업이 끝나면 결과 리스트를 반환
    return result


if __name__ == '__main__':
    pprint(vote_average_movies())    

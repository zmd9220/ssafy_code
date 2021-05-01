import requests
from tmdb import URLMaker


def popular_count():
    # URLMaker 클래스를 통해 maker 인스턴스 생성
    maker = URLMaker('031b6156fbe52ee9595fddf7b81190fa')
    # url를 만들기 위해 get_url에 인자를 넣어 url 문자열 생성
    url = maker.get_url(region='KR', language='ko')
    # 해당 문자열을 토대로 requests.get을 통해 해당 url 페이지의 정보를 가져옴(res로)
    res = requests.get(url) 
    # 가져온 정보(json)를 딕셔너리로 변환
    popular_movies = res.json()

    # 해당 페이지를 본 결과, results에 리스트에 담겨있는 각 아이템들이 영화들에 대한 정보
    # 즉 results의 크기가 총 영화 갯수와 같음
    return len(popular_movies['results'])

if __name__ == '__main__':
    print(popular_count())
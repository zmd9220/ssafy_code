import requests
from tmdb import URLMaker
from pprint import pprint
from operator import itemgetter, attrgetter

def ranking():
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
    
    # itemgetter(평점)을 기준으로 ['results'] 안에 있는 데이터 들을 정렬합니다. 
    # 다만 정렬시 기본은 오름 차순이므로 내림 차순으로 변환해주면 리스트를 뽑아내기 편리합니다. 
    # 그러므로 reverse를 통해 정렬 순서를 뒤집습니다.
    vote_rank_list = sorted(popular_movies['results'], key=itemgetter('vote_average'), reverse=True)

    # 상위 5개의 리스트만 뽑아낼 것이므로 범위를 5로 하여 뽑기
    for i in range(5): 
        # 평점 1위 부터 5위 까지의 영화 제목을 결과 리스트에 담기
        result.append(vote_rank_list[i]['title'])

    # 모든 작업이 끝나면 결과 리스트를 반환
    return result


if __name__ == '__main__':
    # popular 영화 평점순 5개 출력
    pprint(ranking())
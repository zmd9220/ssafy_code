import requests
from tmdb import URLMaker
from pprint import pprint


def credits(title):
    # 결과를 담을 딕셔너리 생성
    result = {} 
    # 배우 리스트, 감독 리스트를 담을 리스트 생성
    cast = []
    crew = []
    # URLMaker 클래스를 통해 maker 인스턴스 생성
    maker = URLMaker('031b6156fbe52ee9595fddf7b81190fa')
    # 영화 제목을 토대로 movie_id 메소드를 사용하여 해당 영화의 id를 찾아 내기
    title_id = maker.movie_id(title)
    # 올바르지 않은 영화 제목을 검색할 경우 title_id에 None이 반환되므로 
    # title_id = None이라는 뜻은 잘못된 영화 제목 검색으로 인해 id가 없을 때
    if title_id == None:
        # id 가 없을 때 None 반환
        return None

    # E번 부터는 아예 클래스에서 movie_id가 들어간 url을 만드는 메소드를 만들어서 사용함
    credit_url = maker.get_plusid_url(title_id, feature='credits', language='ko')
    # 해당 문자열을 토대로 requests.get을 통해 해당 url 페이지의 정보를 가져옴(res로)
    res = requests.get(credit_url) 
    # 가져온 정보(json)를 딕셔너리로 변환
    credit_list = res.json()
    
    for credit in credit_list['cast']:
        # 배우 이면서 cast_id가 10보다 작은 경우
        if credit['known_for_department'] == 'Acting' and credit['cast_id'] < 10:
            # 배우 리스트에 넣기
            cast.append(credit['name'])
    
    for credit in credit_list['crew']:
        # 영화 감독인 경우
        if credit['department'] == 'Directing':
            # 감독 리스트에 넣기
            crew.append(credit['name'])

    
    # 모든 작업이 끝나면 배우, 감독 리스트를 result 딕셔너리에 넣기
    result['cast'] = cast
    result['crew'] = crew

    # 모든 리스트가 들어간 result 딕셔너리를 반환
    return result





if __name__ == '__main__':
    # id 기준 주연배우 감독 출력
    pprint(credits('기생충'))
    # => 
    # {
    #     'cast': [
    #         'Song Kang-ho',
    #         'Lee Sun-kyun',
    #         'Cho Yeo-jeong',
    #         'Choi Woo-shik',
    #         'Park So-dam',
    #         'Lee Jung-eun',
    #         'Chang Hyae-jin'
    #     ],
    #      'crew': [
    #         'Bong Joon-ho',
    #         'Han Jin-won',
    #         'Kim Seong-sik',
    #         'Lee Jung-hoon',
    #         'Park Hyun-cheol',
    #         'Yoon Young-woo'
    #     ]
    # } 
    pprint(credits('id없는 영화'))
    # => None
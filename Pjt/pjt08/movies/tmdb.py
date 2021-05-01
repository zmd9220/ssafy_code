import requests


class URLMaker:    
    url = 'https://api.themoviedb.org/3'

    def __init__(self, key):
        self.key = key

    def get_url(self, category='movie', feature='popular', **kwargs):
        url = f'{self.url}/{category}/{feature}'
        url += f'?api_key={self.key}'

        for k, v in kwargs.items():
            url += f'&{k}={v}'

        return url
    # URLMaker에 중간에 영화 id가 들어가는 api 사용시 만들 url 생성 함수를 만들었습니다.   
    def get_plusid_url(self, mv_id, category='movie', feature='popular', **kwargs):
        url = f'{self.url}/{category}/{mv_id}/{feature}'
        url += f'?api_key={self.key}'

        for k, v in kwargs.items():
            url += f'&{k}={v}'

        return url

    def movie_id(self, title):
        url = self.get_url('search', 'movie', region='KR', language='ko', query=title)
        res = requests.get(url)
        movie = res.json()
        
        if len(movie.get('results')):
            return movie.get('results')[0].get('id')
        else:
            return None
    
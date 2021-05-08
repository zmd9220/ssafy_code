# 알고리즘을 적용한 서버 구성 by 안병진



## 프로젝트 목표

- 데이터를 생성, 조회, 수정, 삭제 할 수 있는 Web Application 제작
- AJAX통신과 JSON 구조에 대한 이해
- Database 1:N, M:N 관계의 이해와 데이터 관계 설정
- 추천 알고리즘 작성



## 개발 환경 및 사용 데이터

- 개발 언어 - Python 3.8.7
- 개발 환경 - Windows 10 64bit, vscode
- 사용 라이브러리 - requirements.txt 참조
- 개발 팀원 - 안병진, 조웅현



## 요구사항

> 커뮤니티 서비스의 상세 기능 개발을 위한 단계로, 모델간의 관계 설정 후 AJAX 통신을 활용하여 UI/UX를 개선합니다.



### A. 프로젝트 구조

> pjt09/은 startproject 명령어로 생성되는 project 디렉토리입니다. 
>
> community/는 startapp 명령어로 생성되는 application 디렉토리입니다. 
>
> 아래의 폴더구조는 주요한 폴더와 파일만 명시되어 있습니다.

#### 🙄 명세서를 읽고 든 생각

- 처음 프로젝트 생성 후 기본 세팅을 하는 작업이었습니다. 이번 프로젝트는 대부분의 틀이 제공되어 있었으므로 받아서 기본 세팅만 하면 됐습니다.

#### 📋 작업 순서

1. 제공받은 프로젝트 파일을 실행합니다.
2. venv를 통해 가상환경 설정 및 실행 후 가상환경에 requirements를 통해 라이브러리를 설치해줍니다.
3. 주어진 데이터 모델로 테이블을 생성합니다.

#### 📰 실제 코드

```bash
$ python -m venv venv
$ source venv/Scrips/activate
$ pip install -r requirements.txt
$ python manage.py migrate
```

#### 💡 느꼈던 점이나 어려웠던 부분, 추가사항

- 이번에는 대부분의 기능을 주어진채로 진행했으므로 간단한 세팅만 해주면 끝이었습니다.

#### 📇 결과

![2021-05-07_17-16-51](README.assets/2021-05-07_17-16-51.png)

---



### B. Model

> 데이터베이스에서 모델의 ERD(Entity Relation Diagram) 예시는 아래와 같습니다.

#### 📋 작업 순서

1. 미리 제공이 다 되어있어서 수정할 필요가 없었습니다.



#### 💡 느꼈던 점이나 어려웠던 부분, 추가사항

- 이 부분은 미리 제공되어서 특별히 한 것이 없습니다.



---



### C. URL

> URL은 app_name과 name을 설정하여 적용합니다.
>
> community app의 모든 URL 패턴은 community/로 시작합니다.
>
> accounts app의 모든 URL 패턴은 accounts/로 시작합니다.
>
> movies app의 모든 URL 패턴은 movies/로 시작합니다.

#### 📋 작업 순서

1. 이 부분도 미리 제공되어 있었기 때문에 별도로 작업할 것이 없었습니다.


#### 💡 느꼈던 점이나 어려웠던 부분, 추가사항

- 사전에 제공된 데이터를 그대로 사용했습니다.



---





## D. View & Template



### 들어가기전

> Axios를 전체 html에서 사용하기 위해 base.html에서 해당 Axios CDN을 추가했습니다.

```django
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
```



### D-1 리뷰 좋아요 기능

> 1. 전체 리뷰 조회 페이지에 각 리뷰의 좋아요 버튼과 좋아요 개수를 출력합니다.
> 2. 이미 좋아요 버튼을 누른 경우 취소 버튼을 출력합니다.
> 3. 인증된 사용자만 리뷰에 좋아요 할 수 있습니다.
> 4. 좋아요 버튼을 클릭하는 경우 AJAX통신을 이용하여 서버에서 JSON데이터를 받아와 상황에 맞게 HTML화면을 구성합니다.

#### 📋 작업 순서

1. 명세에 맞게 view를 수정합니다. (JSON 데이터를 받기 위해)
2. JSON 데이터를 받아 js로 처리를 한 뒤, index.html에서 좋아요에 해당하는 부분을 수정하여 실시간으로 반영 될 수 있도록 변경합니다.

#### 📰 실제 코드

```python
# views.py
@require_POST
def like(request, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        user = request.user

        if review.like_users.filter(pk=user.pk).exists():
            review.like_users.remove(user)
            liked = False
        else:
            review.like_users.add(user)
            liked = True
        response_data = {
            'liked': liked,
            'count': review.like_users.count(),
        }
    #     return redirect('community:index')
        return JsonResponse(response_data)
    # return redirect('accounts:login')
    return HttpResponse(status=401)
```

```django
{% extends 'base.html' %}

{% block content %}
  <h1>Community</h1>
  {% if user.is_authenticated %}
    <a href="{% url 'community:create' %}">NEW</a>
  {% else %}
    <a href="{% url 'accounts:login' %}">[새 글을 작성하려면 로그인하세요]</a>
  {% endif %}
  <hr>
  {% for review in reviews %}
    <p><b>작성자 : <a href="{% url 'accounts:profile' review.user.username %}">{{ review.user }}</a></b></p>
    <p>글 번호: {{ review.pk }}</p>
    <p>글 제목: {{ review.title }}</p>
    <p>글 내용: {{ review.content }}</p>
    <form class="like-form" data-review-id="{{ review.pk }}" class="d-inline">
      {% csrf_token %}
      {% if user in review.like_users.all %}
        <button id="like-btn-{{ review.pk }}" class="btn btn-link">
          <i id="like-icon-{{ review.pk }}" class="fas fa-heart fa-lg" style="color:crimson;"></i>
        </button>
      {% else %}
        <button id="like-btn-{{ review.pk }}" class="btn btn-link">
          <i id="like-icon-{{ review.pk }}" class="fas fa-heart fa-lg" style="color:black;"></i>
        </button>
      {% endif %}
    </form>
    <span id="like-count-{{ review.pk }}">{{ review.like_users.all|length }}</span> 명이 이 글을 좋아합니다.<br>
    <a href="{% url 'community:detail' review.pk %}">[detail]</a>
    <hr>
  {% endfor %}
  <script>
    const forms = document.querySelectorAll('.like-form')
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value
    forms.forEach(form => {

      form.addEventListener('submit', event => {
        event.preventDefault()
        const reviewId = event.target.dataset.reviewId

        // 새롭게 config 방법으로 post를 보낼 것 axios(config)
        // https://github.com/axios/axios#request-config
        axios({
          url: `/community/${reviewId}/like/`,
          method: 'post',
          headers: {
            'X-CSRFToken': csrfToken,
          },
        }).then( function (response) {
          console.log(response.data)
          const { liked, count } = response.data
          // 내가 좋아요를 눌렀는지 여부
          const likeIcon = document.querySelector(`#like-icon-${reviewId}`)
          likeIcon.style.color = liked ? 'crimson' : 'black'
          // 몇 명이 좋아하는지
          const likeCount = document.querySelector(`#like-count-${reviewId}`)
          likeCount.innerText = count
        }).catch( function (error) {
          console.log(error.response)
          switch (error.response.status) {
            case 401: {
              // 로그인 페이지로 보내준다.
              location.href = '/accounts/login/'
              break
            }
            default: {
              // 위에서 처리하지 않은 모든 에러 메세지를 경고창으로 표시한다.
              alert('알 수 없는 에러가 발생했습니다. 관리자를 통해 문의해주세요.')
            }
          }

        })
         
      })
    })
  </script>
{% endblock %}
```

#### 💡 느꼈던 점이나 어려웠던 부분, 추가사항

- 이번 주에 배웠던 기능중 하나인 좋아요 부분을 js를 통해 새로고침 없이 동적으로 변경하게 하는 부분을 복습하는 느낌으로 진행했습니다.
- 이 부분은 네비게이터로써 진행했는데, 기존에 배웠던 내용에선 버튼의 텍스트를 바꾼다면 이번에는 버튼의 icon 태그를 바꿔야해서 icon 태그로 직접 접근하여 바꿨습니다. 순간 어떻게 구현해야하나 막막했지만 침착하게 잘 해낸 것 같습니다. 또 바닐라 자바스크립트가 아직 익숙치 않아 구현할 때 있어서 아직 막히는 곳이 많은 것 같아 연습이 필요한 것 같습니다.

#### 📇 결과

![2021-05-07_17-33-20](README.assets/2021-05-07_17-33-20.png)

---





### D-2 유저 팔로우 기능

> 1. 사용자 상세 페이지에 팔로우 버튼과 팔로우수를 출력합니다.
> 2. 이미 팔로우 버튼을 누른 경우 취소 버튼을 출력합니다.
> 3. 인증된 사용자만 팔로우 할 수 있습니다.
> 4. 로그인한 사용자 자신은 팔로우 할 수 없습니다.
> 5. 좋아요 버튼을 클릭하는 경우 AJAX통신을 이용하여 서버에서 JSON데이터를 받아와 상황에 맞게 HTML화면을 구성합니다.

#### 📋 작업 순서

1. 명세에 맞게 view를 수정합니다. (JSON 데이터를 받기 위해)
2. JSON 데이터를 받아 js로 처리를 한 뒤, _follow.html 팔로우에 해당하는 부분을 수정하여 실시간으로 반영 될 수 있도록 변경합니다.
3. profile.html에서 include를 통해 _follow.html이 나오도록 연결해줍니다.

#### 📰 실제 코드

```python
# views.py
@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        person = get_object_or_404(get_user_model(), pk=user_pk)
        user = request.user
        if person != user:
            if person.followers.filter(pk=user.pk).exists():
                person.followers.remove(user)
                follow = False
            else:
                person.followers.add(user)
                follow = True
        response_data = {
            'follow' : follow,
            'fiCnt' : user.followers.count(),
            'fwCnt' : user.followings.count(),
        }
        return JsonResponse(response_data, status=200)
    return HttpResponse(status=401)
```

```django
<!-- _follow.html -->
<div class="jumbotron text-center text-white bg-dark">
  <p class="lead mb-1">작성자 정보</p>
  <h1 class="display-4">{{ person.username }}</h1>
  <hr>
  {% with followings=person.followings.all followers=person.followers.all %}
    <p class="lead">
      팔로잉 : <span id="following-cnt-{{ person.pk }}">{{ followings|length }}</span>
       / 팔로워 : <span id="follower-cnt-{{ person.pk }}">{{ followers|length }}</span>
    </p>
    <!-- 팔로우 버튼 -->
    {% if request.user != person %}
      <!-- js로 처리할 것이기 때문에, form에 url이 포함될 필요가 없다. 
        data-userpk를 통해, 속성에 사용자 pk를 저장할 수 있다.
      -->
      <form class="follow-form" data-user="{{ user.username }}" data-userpk="{{ person.pk }}">
        {% csrf_token %}
        <button id="follow-button-{{ person.pk }}">
          {% if request.user in followers %}
            Unfollow
          {% else %}
            Follow
          {% endif %}
        </button>
      </form>
    {% endif %}
  {% endwith %}

  <script>
    form = document.querySelector('.follow-form')
    // csrf토큰을 별도로 저장해야 한다. 이름은 csrfmiddlewaretoken이다.
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value
    form.addEventListener('submit', function (event) {
      event.preventDefault()

      const userpk = event.target.dataset.userpk
      const user = event.target.dataset.user
      axios({
        url: `/accounts/follow/${ userpk }/`,
        method: 'POST',
        headers: {
          'X-CSRFToken' : csrfToken,
        },
      }).then((response) => {
        const { follow, fiCnt, fwCnt } = response.data
        const followBtn = document.querySelector(`#follow-button-${ userpk }`)
      
        followBtn.innerText = follow ? '팔로우 취소' : '팔로우'
        const followingCnt = document.querySelector(`#following-cnt-${ userpk }`)
        const followerCnt = document.querySelector(`#follower-cnt-${ userpk }`)
        followingCnt.innerText = fiCnt
        followerCnt.innerText = fwCnt
      }).catch((error) => {
        switch(error.response.status) {
          case 401: {
            location.href = `/accounts/login/`
            break
          }
          default: {
            alert(error)
          }
        }
      })
    })
  </script>
</div>
```

```django
<!-- profile.html -->
<h1 class="text-center">{{ person.username }}님의 프로필</h1>

{% include 'accounts/_follow.html' %}
```

#### 💡 느꼈던 점이나 어려웠던 부분, 추가사항

- 이 부분은 드라이버로서 진행했습니다. 팀원분이 기능별로 깔끔하게 나눠서 (_follow.html) 진행하였는데, 제가 봤을 때 괜찮은 방법이라고 생각했습니다. 만약 다음에 프로젝트 하게 된다면 저도 기능을 나눠서 만들고 include로 합치는 방법을 한 번 사용해보려고 합니다. 
- 전반적으로 지시가 스무스하기도 했고, 복습하는 느낌이 강해서 큰 막힘없이 진행했던 것 같습니다.

#### 📇 결과

- 팔로우 전

![2021-05-07_17-40-39](README.assets/2021-05-07_17-40-39.png)

- 팔로우 후

![2021-05-07_17-40-33](README.assets/2021-05-07_17-40-33.png)

---





### D-3 추천 알고리즘 작성 + 추가적인 Styling

> 1. 사용자에게 응답으로 제공할 HTML은 recommended.html입니다.
> 2. 인증된 사용자에게 10개의 영화를 추천하여 제공합니다.
> 3. Bootstrap을 활용하여 자유롭게 스타일링 합니다.

#### 📋 작업 순서

1. 추천 제공을 해당 영화의 상세 페이지로 들어갔을 때 해당 영화의 장르를 찾아 같은 장르의 영화 데이터를 찾고, 그 중 랜덤으로 10개를 뽑아 데이터를 js에 제공합니다.
2. js를 통해 가공하여 영화 상세 페이지 하단에 보여주도록 합니다. 제공되는 데이터는 부트스트랩 grid를 이용하여 한 줄에 4개 씩 보여주도록 하였습니다.

#### 📰 실제 코드

```python
# views.py
@require_GET
def recommended(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    genre_list = movie.genres.all() # 정참조. 영화에 해당하는 장르 목록 가져오기.

    g_list = []
    for g in genre_list:
        g_list.append(g.pk)
    
    pick_genre = random.sample(g_list, 1)
    
    genre = get_object_or_404(Genre, pk=pick_genre[0])
    movie_list = genre.movie_set.all().order_by('?')[:10] # 역참조. 10개만 가져오기.

    response_data = serializers.serialize('json', movie_list)
    return HttpResponse(response_data, status=200)
```

```django
<!-- detail.html -->
{% extends 'base.html' %}
  
{% block content %}

  <h1>{{ movie.title }}</h1>
  <p>
    <span id="mySpan" data-movieId="{{ movie.pk }}">
    {% for genre in movie.genres.all %}
    {{ genre.name }}
    {% endfor %}
    </span>
  </p>
  <p>popularity : {{ movie.popularity }}</p>
  <p>vote average : {{ movie.vote_average }}</p>
  <p>overview : {{ movie.overview }}</p>
  <img src="{{ movie.poster_path }}" alt="">
  <hr>
  <h3>추천 영화 목록</h3>
  <div class="container">
    <div id="rMovies" class="row">
    
    </div>
  </div>
  <script>
  const mySpan = document.querySelector('#mySpan')
  const movieId = mySpan.dataset.movieid
  
  axios({
    url: `/movies/recommended/${ movieId }`,
    data: "GET",
  }).then((response) => {
    console.log(response.data)
    response.data.forEach((movie) => {
      const movieList = document.querySelector('#rMovies')
      const movieDiv = document.createElement('div')
      movieDiv.setAttribute('class', 'col-3')
      movieDiv.classList.add('rMovie')

      const MovieHTML = `
        <h7>${ movie.fields.title }</h7><br>
        <img src="${ movie.fields.poster_path }" width='100px' height='200px'></img>
      `
      movieDiv.innerHTML = MovieHTML
      movieList.appendChild(movieDiv)
    })
  })
  </script>
  <style>
  .rMovie{ 
    margin-right : auto;
  }
  </style> 
{% endblock %}
```

#### 💡 느꼈던 점이나 어려웠던 부분, 추가사항

- 영화 상세 페이지의 장르를 토대로 추천 영화 목록을 작성하였기에 recommended.html 은 사용하지 않고 detail.html 안에서 밑에 목록을 추가하는 방식으로 진행하였습니다.
- 처음에는 영화 페이지의 장르를 토대로 역참조를 한 뒤, 해당 id를 토대로 같은 장르를 가진 영화 목록을 가져오면 될 거라고 생각했는데, db 관련 파트를 다루는게 오랜만이다 보니 어색하기도 기억이 잘 나지 않아서 굉장히 진행이 오래걸렸습니다.
- 느낀것은 아무래도 db에 대한 지식이 많이 부족하다고 느꼈고, 자유롭게 쓸 수 있을 정도로 연습이 필요하겠다고 생각했습니다.

#### 📇 결과

![2021-05-07_17-41-18](README.assets/2021-05-07_17-41-18.png)

---


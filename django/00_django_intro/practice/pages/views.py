from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def fake_google(request):
    return render(request, 'pages/fake-google.html')


def introduce(request, name, age):
    context = {
        'name': name,
        'age': age,
    }
    return render(request, 'pages/introduce.html', context)

# 사용자 정보를 입력받는 throw.html 랜더링
def throw(request):
    return render(request, 'pages/throw.html')

# 사용자 정보를 받아서 처리하는 로직
def catch(request):

    # throw를 통해 전달한 정보를 꺼낸다.
    # form 형태는 request속에 값을 넣어 보냄, 그리고 기본 보내는 method는 GET, 다른경우 POST
    # 전달오는 데이터는 딕셔너리고 에러를 내지않기 위해 .get을 사용
    content = request.GET.get('content')

    context = {
        'content': content
    }

    return render(request, 'pages/catch.html', context)


    
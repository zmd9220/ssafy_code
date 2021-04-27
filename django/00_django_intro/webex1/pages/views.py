from django.shortcuts import render

# Create your views here.
# 요청을 받으면 index.html을 응답하는 함수
def index(request):
    
    context = {
        'message' : 'hello world'
    }

    # Response
    return render(request, 'index.html', context)


def mylist(request):
    students = [
        '김싸피',
        '이싸피',
        '박싸피',
    ]

    context = {
        'students': students,
    }
    return render(request, 'mylist.html', context)

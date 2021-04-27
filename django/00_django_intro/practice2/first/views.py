from django.shortcuts import render
# Create your views here.

def throw(request):

    return render(request, 'first/throw.html')

def catch(request):
    
    context = {
        'name':request.GET.get('name'),
        'age':request.GET.get('age'),
    }
    return render(request, 'first/catch.html', context)
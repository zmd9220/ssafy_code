from django.shortcuts import render

# Create your views here.
def introduce(request, name, age):
    
    context = {
        'name':name,
        'age':age,
    }
    return render(request, 'second/introduce.html', context)
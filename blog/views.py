from django.shortcuts import render
from . import forms

def test(request):
    m = ''
    form = forms.Test()
    if form.is_valid():
        forms.Test()
    
    context = {
        "form":form,
        'output':m
    }
    return render(request, 'test.html',context)

def index(request):
    return render(request, 'index.html')

def courses(request):
    return render(request, 'courses.html')

def files(request):
    return render(request, 'files.html')

def plans(request):
    return render(request, 'plans.html')

def profile(request):
    return render(request, 'profile.html')

def projects(request):
    return render(request, 'projects.html')

def settings(request):
    return render(request, 'settings.html')

def friends(request):
    return render(request, 'friends.html')


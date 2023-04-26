from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from . import forms
# @csrf_exempt
# def add(request):
#     if request.method == 'POST':
#         x = int(request.POST.get('firstvalue'))
#         y = int(request.POST.get('secondvalue'))
#         z = x + y
#         return HttpResponse('Result = ' + str(z))
#     else:
#         return HttpResponse('''
#     <form action="hi" method="post">
#         <p>
#             <label for="firstvalue"> enter first number:</label>
#             <input type="text" name="firstvalue" id="">
#         </p>
#         <p>
#             <label for="secondvalue"> enter second number:</label>
#             <input type="text" name="secondvalue" id="">
#         </p>
#         <button type="submit">ADD</button>
#     </form>
#                             ''')
        
        
        
        

def addition(request):
    form = forms.InputForm()
    z = 0
    if request.method == "POST":
        form = forms.InputForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            x = cd['x']
            y = cd['y']
            z = x + y
            
    
    context = {
        'form': form ,
        'output': z
    }
    return render(request, 'add.html',context)
def Subtract(request):
    form = forms.InputForm()
    z = 0
    if request.method == "POST":
        form = forms.InputForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            x = cd['x']
            y = cd['y']
            z = x - y
            
    
    context = {
        'form': form ,
        'output': z
    }
    return render(request, 'Subtract.html',context)
def hit(request):
    form = forms.InputForm()
    z = 0
    if request.method == "POST":
        form = forms.InputForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            x = cd['x']
            y = cd['y']
            z = x * y
            
    
    context = {
        'form': form ,
        'output': z
    }
    return render(request, 'hit.html',context)
def portion(request):
    form = forms.InputForm()
    z = 0
    if request.method == "POST":
        form = forms.InputForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            x = cd['x']
            y = cd['y']
            z = x / y
            
    
    context = {
        'form': form ,
        'output': z
    }
    return render(request, 'portion.html',context)


def index(request):
    return render(request, 'index.html')

from ctypes.wintypes import HHOOK

from django.shortcuts import render
from django.http import HttpResponse
from django.template.backends.django import reraise
import random
import string

def home(request):
    return render(request, 'base.html')
def index(request):
    return HttpResponse("<p> Hello, world. You're at the polls index.</p>")

def factorial(request):
    number = int(request.GET.get('number', 10))
    result = 1
    for i in range(1,number+1):
        result *= i
    return HttpResponse(f"<h1>Result:{result}</h1>")

def info(request):
    print(request.GET)
    return HttpResponse(
        f"<h1>Info</h1><br>"
        f"<p>{request.build_absolute_uri()}</p>"
        f"<p>{request.method}</p>"
        f"<p>{request.GET['name']}<br>Age: {request.GET['Age']}</p>"
    )


def task_1(request):
    name = request.GET.get('name','Islambek')
    return render(request,'blog/task_1.html',{'name':name})

def task_7(request):
    number = int(request.GET.get('n',5))
    numbers = range(1,11)
    context = [f'{number}x{i} = {number * i}' for i in range(1,11)]
    return render(request, 'blog/task_7.html', {'number':number,'context':context})

def task_2(request):
    a = int(request.GET.get('a',0))
    b = int(request.GET.get('b',0))
    return render(request, 'blog/task_2.html', {'a': a, 'b': b, 'result': a + b})

def task_3(request):
    number = int(request.GET.get('number', 9))
    var_ = False
    if number %  2 == 0:
        var_ = True
    else:
        var_ = False
    return render(request, 'blog/task_3.html',{'number':number, 'var':var_})

def task_4(request):
    words = request.GET.get('words','Macbook')
    n = int(request.GET.get('n',5))
    word_list = words.split()
    updated_list = [i for i in word_list if len(i) > n]
    return render(request, 'blog/task_4.html', {'words':words,'n':n,'word_list':word_list,'filtered_list':updated_list})

def task_5(request):
    word = request.GET.get('word','apa')
    condition = True
    if word != word[::-1]:
        condition = False
    return render(request, 'blog/task_5.html',{'check':condition,'word':word})

def task_6(request):
    birth_year = int(request.GET.get('year',2007))
    age = 2025-birth_year
    return render(request, 'blog/task_6.html',{'age':age})

def task_8(request):
    nums=request.GET.get('nums','12,14,29,76')
    num_list = nums.split(',')
    max=0
    for i in num_list:
        if int(i)>max:
            max = int(i)
    return render(request, 'blog/task_8.html',{'max':max})

def task_9(request):
    celcius=int(request.GET.get('celcius',0))
    farenheit = (celcius*9/5)+32
    return render(request, 'blog/task_9.html',{'C':celcius,'F':farenheit})

def task_10(request):
    length = int(request.GET.get('length',8))
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length+1))
    return render(request, 'blog/task_10.html',{'password':password,'length':length})
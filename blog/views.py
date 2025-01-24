from ctypes.wintypes import HHOOK

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.template.backends.django import reraise
import random
import string

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

def hello(request):
    name = request.GET.get('name','Гость')
    greeting = f"<p>Hello, {name}! Welcome to our site.</p>"

    return HttpResponse(greeting)


def sum(request):
    try:
        a = float(request.GET['a'])
        b = float(request.GET['b'])
    except (KeyError, ValueError):
        return JsonResponse({'error': 'Both parameters a and b must be valid numbers and are required.'}, status=400)

    result = a + b

    return JsonResponse({'a': a, 'b': b, 'sum': result})


def check_number(request):
    number = request.GET.get('number')

    if number is not None and number.isdigit():
        number = int(number)

        if number % 2 == 0:
            return HttpResponse(f"{number}--> even numbers")
        else:
            return HttpResponse(f"{number}--> odd numbers")

    else:
        return HttpResponse("Please provide a valid number via the 'number' parameter.")




def filter_words(request):
    text = request.GET.get('text', '')
    n = int(request.GET.get('n', 0))

    words = text.split()

    filtered_words = [word for word in words if len(word) > n]

    return JsonResponse(filtered_words, safe=False)


def palindrome(request):
    word = request.GET.get('word', '')

    if word == word[::-1]:
        return HttpResponse(f'Word {word} is a palindrome')
    else:
        return HttpResponse(f'Word {word} is not a palindrome')

def age_old(request):
    year_old = request.GET.get('year_old', '')

    if not year_old:
        return HttpResponse("Please indicate the year of birth using the 'year' parameter.")

    if not year_old.isdigit():
        return HttpResponse("Invalid year format. Please enter an integer.")

    birth_year = int(year_old)
    current_year = 2025 or 2024
    age = current_year - birth_year

    if age < 0:
        return HttpResponse(f"The year of birth is incorrect.")

    return HttpResponse(f'Your age: {age} years')




def multiplication(request):
    param = request.GET.get('n','')
    if not param:
        return HttpResponse("Please specify a number using the 'n' parameter.")
    if not param.isdigit():
        return HttpResponse("Invalid number format. Please enter an integer.")

    n = int(param)
    table = [f'{n} x {i} = {n * i}' for i in range(1,11)]
    response = "<br>".join(table)

    return HttpResponse(response)


def find_maximum(request):
    numbers_param = request.GET.get('numbers', '')
    if not numbers_param:
        return HttpResponse("Please provide a list of numbers using the 'numbers' parameter.")

    try:
        numbers = [int(num.strip()) for num in numbers_param.split(',')]
    except ValueError:
        return HttpResponse("Invalid number format. Please provide a list of numbers separated by commas.")

    if not numbers:
        return HttpResponse("The list of numbers is empty. Please provide at least one number.")

    maximum_number = max(numbers)

    return HttpResponse(f"The maximum number is: {maximum_number}")


def convert_temperature(request):
    celsius_param = request.GET.get('celsius', '')
    if not celsius_param:
        return HttpResponse("Please provide a temperature in Celsius using the 'celsius' parameter.")

    try:
        celsius = float(celsius_param)
    except ValueError:
        return HttpResponse("Invalid temperature format. Please provide a numeric value for Celsius.")

    fahrenheit = (celsius * 9/5) + 32

    return HttpResponse(f"{celsius}°C = {fahrenheit}°F")


def generate_password(request):
    length_param = request.GET.get('length', '')
    if not length_param:
        return HttpResponse("Please provide the password length using the 'length' parameter.")

    if not length_param.isdigit():
        return HttpResponse("Invalid length format. Please provide a numeric value for the password length.")

    length = int(length_param)
    if length <= 0:
        return HttpResponse("Password length must be greater than 0.")

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))

    return HttpResponse(f"Your password: {password}")
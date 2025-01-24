from django.urls import path
from . import views
urlpatterns = [
    path('index/', views.index),
    path('factorial/', views.factorial),
    path('info/', views.info),
    path('hello/', views.hello),
    path('calculate/', views.sum),
    path('check/', views.check_number),
    path('filter_words/', views.filter_words),
    path('palindrome/', views.palindrome),
    path('age_old/', views.age_old),
    path('multiplication/', views.multiplication),
    path('max/', views.find_maximum),
    path('temperature/', views.convert_temperature),
    path('password/', views.generate_password),
]

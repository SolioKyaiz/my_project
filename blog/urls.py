from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('index/', views.index),
    path('factorial/', views.factorial),
    path('info/', views.info),
    path('task-1/', views.task_1,name = 'task-1'),
    path('task-2/', views.task_2,name = 'task-2'),
    path('task-3/', views.task_3,name = 'task-3'),
    path('task-4/', views.task_4,name = 'task-4'),
    path('task-5/', views.task_5,name = 'task-5'),
    path('task-6/', views.task_6,name = 'task-6'),
    path('task_7/', views.task_7,name = 'task-7'),
    path('task-8/', views.task_8,name = 'task-8'),
    path('task-9/', views.task_9,name = 'task-9'),
    path('task-10/', views.task_10,name = 'task-10'),
]

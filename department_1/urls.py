from django.urls import path
from department_1.views import *


urlpatterns = [
    path('', index, name='index'),


    ]

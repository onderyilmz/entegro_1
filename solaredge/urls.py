from django.urls import path
from solaredge.views import *


urlpatterns = [
    path('', index, name='index'),


    ]

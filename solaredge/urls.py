from django.urls import path
from solaredge.views import (
    index,
    second,
    question,
    catchUp,
    customerEdit,
    )

urlpatterns = [
    path('', index, name='index'),
    path('second/', second, name='second'),
    path('question/', question, name='question'),

    path('catchUp/', catchUp, name='catchUp'),



    path('customerEdit/', customerEdit, name='customerEdit'),

    ]
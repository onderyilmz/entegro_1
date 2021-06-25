from django.urls import path
from department_1.views import (
    index,
    second,
)

urlpatterns = [
    path('', index, name='index'),
    path('second/', second, name='second'),

]
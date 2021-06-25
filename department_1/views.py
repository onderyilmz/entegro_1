from django.shortcuts import render

# Create your views here.



def index(request):
    context = dict()


    context['menu'] = 'index'
    return render(request, 'department_1/index.html', context) 


def second(request):
    context = dict()


    context['menu'] = 'second'
    return render(request, 'department_1/second.html', context) 


from django.shortcuts import render
# Create your views here.



def index(request):
    context = dict()

    context['menu'] = 'index'
    return render(request, 'solaredge/index.html', context)


def second(request):
    context = dict()

    context['menu'] = 'second'
    return render(request, 'solaredge/second.html', context)



def question(request):
    context = dict()

    return render(request, 'solaredge/question.html', context)
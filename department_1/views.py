from django.shortcuts import render

# Create your views here.



def index(request):
    context = dict()

    return render(request, 'department_1/index.html')
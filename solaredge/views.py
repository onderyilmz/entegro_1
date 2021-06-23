from django.shortcuts import render

# Create your views here.

import datetime




def index(request):
    context = dict()

    suAn = datetime.datetime.now()
    tarih_strftime = datetime.datetime.strftime(suAn, '%d %B %Y')



    return render(request, 'solaredge/index.html')
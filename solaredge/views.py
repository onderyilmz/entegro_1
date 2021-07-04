from django.shortcuts import render, redirect
from solaredge.models import Scoring, Questions, Customer, QuestionChoice, Questions2, Scoring2
from solaredge.forms import ReadForm, GeeksForm
# Create your views here.
from django.forms import modelformset_factory
from .forms import CHOICES, QForm
from django.contrib import messages

def index(request):
    context = dict()

    context['que'] = Questions2.objects.all()
    context['customer'] = Customer.objects.all()
    context['form'] = CHOICES(request.POST)
    # Burada çarpan olarak gelen alanı çarpıp kayıt etme işlemini öyle yapabilirz
    if request.method == 'POST':
        if request.POST.get('coursee'):
            saver = Scoring2()
            saver.customer = request.POST.get('coursee')
            saver.note = request.POST.get('w3review')

            #saver.customer = request.POST.get('chkvalues1')

            saver.save()
            messages.success(request, 'Bu işlem tamamlandı' + request.POST.get('coursee'))

            return render(request, 'solaredge/index.html', context)
    else:
        return render(request, 'solaredge/index.html', context)

"""
    form = CHOICES(request.POST)
    form2 = QForm(request.POST)
    print(form2)
    if form.is_valid():
        selected = form.cleaned_data.get("NUMS")
        selected1 = form.cleaned_data.get("model_choice")

        print(selected)
        print(selected1)


    context['customer'] = customer
    context['ques'] = ques
    context['form'] = form
    context['form2'] = form2

    return render(request, 'solaredge/index.html', context)
"""



def second(request):
    context = dict()

    context['menu'] = 'second'
    return render(request, 'solaredge/second.html', context)


def question(request):
    context = dict()
    context['puan'] = QuestionChoice.objects.all()
    context['customer'] = Customer.objects.all()

    context['skorlar'] = Questions.objects.all()
    return render(request, 'solaredge/question.html', context)

def catchUp(request):
    context = dict()

    if request.method == "POST":
        messageForm = ReadForm(request.POST)
        print(messageForm)

        """
        if messageForm.is_valid():
            messageForm.save()
            note = "Mesajınız için Teşekkürler"
            context['form'] = ReadForm()
            context['note'] = note
            return redirect('index')
        """
    else:

        context['form'] = ReadForm()


    return render(request, 'solaredge/tableQuestion.html', context)


def customerEdit(request):
    context = dict()
    formKayit = modelformset_factory(Questions2, fields=('question', 'options1', 'options2', 'options3', 'options4', 'carpan'))

    if request.method == 'POST':
        form = formKayit(request.POST)
        print(form)
        for i in form:
            print(i)

    return render(request, 'solaredge/customerEdit.html', context)


from django.shortcuts import render
from django.http import HttpResponse
from .forms import SubscriberForm

def basa(request):
    form = SubscriberForm(request.POST or None)
    return render(request, 'main/upmeny/women.html')


def glavnoe(request):
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        data = form.cleaned_data
        new_form = form.save()

    return render(request, 'main/upmeny/glavnoe.html', locals())


def corzina(request):
    return render(request, 'main/upmeny/corzina.html')


def women(request):
    return render(request, 'main/upmeny/women.html')


def men(request):
    return render(request, 'main/upmeny/men.html')


def acsesuariwomen(request):
    return render(request, 'main/nizmenywomen/acsesuari.html')


def newwomen(request):
    return render(request, 'main/nizmenywomen/new.html')


def obuwwomen(request):
    return render(request, 'main/nizmenywomen/obuw.html')


def odezdawomen(request):
    return render(request, 'main/nizmenywomen/odezda.html')


def salewomen(request):
    return render(request, 'main/nizmenywomen/sale.html')


def acsesuarimen(request):
    return render(request, 'main/nizmenymen/acsesuari.html')


def newmen(request):
    return render(request, 'main/nizmenymen/new.html')


def obuwmen(request):
    return render(request, 'main/nizmenymen/obuw.html')


def odezdamen(request):
    return render(request, 'main/nizmenymen/odezda.html')


def salemen(request):
    return render(request, 'main/nizmenymen/sale.html')





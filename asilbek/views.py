from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
# from .models import Zakazlar, Kasb_turi, PraysZakaz, PraysIshchi, Maxsulot, Xodimlar, Etirozlar
# from .forms import ContactForm, MaxsulotForm
from .models import *
from .forms import *


def admin_list(request):
    zakaz_list = Zakazlar.objects.all()
    ishchilar_list = Xodimlar.objects.all()
    maxsulot_list = Maxsulot.objects.all()
    prayszakaz_list = PraysZakaz.objects.all()
    praysishchi_list = PraysIshchi.objects.all()
    kasb_list = Kasb_turi.objects.all()
    etirozlar_list = Etirozlar.objects.all()

    formMaxsulot = MaxsulotForm(request.POST or None)
    formXodimlar = XodimlarForm(request.POST or None)
    formZakaz = ZakazlarForm(request.POST or None)
    formKasb = KasbForm(request.POST or None)
    formCombinate = CombinedForm(request.POST or None)

    if request.method == "POST" and formMaxsulot.is_valid():
        formMaxsulot.save()
        # return HttpResponse("Yangi maxsulot saqlandi")
    if request.method == "POST" and formXodimlar.is_valid():
        formXodimlar.save()
    if request.method == "POST" and formZakaz.is_valid():
        formZakaz.save()
    if request.method == "POST" and formKasb.is_valid():
        formKasb.save()
    if request.method == "POST" and formCombinate.is_valid():
        formCombinate.save()
    else:
        print(formMaxsulot.errors, formXodimlar.errors, formKasb, formZakaz, formCombinate)
    context = {
        "zakaz_list": zakaz_list,
        "ishchilar_list": ishchilar_list,
        "maxsulot_list": maxsulot_list,
        "prayszakaz_list": prayszakaz_list,
        "praysishchi_list": praysishchi_list,
        "kasb_list": kasb_list,
        "etirozlar_list": etirozlar_list,
        "formMaxsulot": formMaxsulot,
        "formZakaz": formZakaz,
        "formKasb": formKasb,
        "formCombinate": formCombinate,
    }

    return render(request, 'pages/admin.html', context)


def ishchilar_page(request):
    zakaz_list = Zakazlar.objects.filter(status__in=[Zakazlar.Status.primary, Zakazlar.Status.danger])
    ishchilar_list = Xodimlar.objects.all()
    formContact = ContactForm(request.POST or None)
    if request.method == "POST" and formContact.is_valid():
        formContact.save()
        return HttpResponse("Thank you!!")
    else:
        print(formContact.errors)

    context = {
        "zakaz_list": zakaz_list,
        "ishchilar_list": ishchilar_list,
        "formContact": formContact,
    }

    return render(request, 'pages/elektrik.html', context)


def magazin_page(request):
    zakaz_list = Zakazlar.objects.filter(status__in=[Zakazlar.Status.primary, Zakazlar.Status.danger])
    maxsulot_list = Maxsulot.objects.all()
    formContact = ContactForm(request.POST or None)
    formMaxsulot = MaxsulotForm(request.POST or None)
    formSavdoTarixi = SavdoTarixiForm(request.POST or None)

    if request.method == "POST":
        if formMaxsulot.is_valid():
            maxsulot_instance = formMaxsulot.save(commit=False)

            # Получить значение soni из формы и сохранить его в SavdoTarixi
            soni_value = request.POST.get('soni')
            savdo_tarixi_instance = SavdoTarixi(
                maxsulot_nomi=maxsulot_instance.maxsulot_nomi,
                maxsulot_soni=soni_value,
                maxsulot_narxi=maxsulot_instance.foiz_narxi
            )
            savdo_tarixi_instance.save()

            # Вычесть значение soni из Maxsulot
            maxsulot_instance.soni -= int(soni_value)
            maxsulot_instance.save()

            # Очистить форму после сохранения, если нужно
            formMaxsulot = MaxsulotForm()
            # return HttpResponse("Yangi maxsulot saqlandi")

    if request.method == "POST" and formSavdoTarixi.is_valid():
        formSavdoTarixi.save()

    if request.method == "POST" and formContact.is_valid():
        formContact.save()
        # return HttpResponse("Thank you!!")
    else:
        print(formMaxsulot.errors, formContact.errors)
    context = {
        "zakaz_list": zakaz_list,
        "maxsulot_list": maxsulot_list,
        "formContact": formContact,
        "formMaxsulot": formMaxsulot,
        "formSavdoTarixi": formSavdoTarixi,
    }

    return render(request, 'pages/do`kon.html', context)

def zakazchi_page(request):
    zakaz_list = Zakazlar.objects.filter(status__in=[Zakazlar.Status.primary, Zakazlar.Status.danger])
    formContact = ContactForm(request.POST or None)
    if request.method == "POST" and formContact.is_valid():
        formContact.save()
        return HttpResponse("Thank you!!")
    context = {
        "zakaz_list": zakaz_list,
        "formContact": formContact,
    }

    return render(request, 'pages/zakazchi.html', context)


def login_page(request):
    return render(request, 'pages/login.html')

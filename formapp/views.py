from django.http import HttpResponse
from django.shortcuts import render
from .models import StageModel

# def index(request):
#     return HttpResponse("Hello World!")

def index(request):
    # header = "Personal Data"  # обычная переменная
    # langs = ["English", "German", "Spanish"]  # массив
    # user = {"name": "Tom", "age": 23}  # словарь
    # addr = ("Абрикосовая", 23, 45)  # кортеж
    # data = {"header": header, "langs": langs, "user": user, "address": addr}
    questions = StageModel.objects.all()

    return render(request, "formapp/formapp.html", context={'questions':questions})
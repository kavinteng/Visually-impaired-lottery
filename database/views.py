from django.shortcuts import render, redirect, reverse
from .models import lottery

def index(request):
    num = lottery.objects.all()

    content = {'num':num}

    return render(request, 'index.html', content)
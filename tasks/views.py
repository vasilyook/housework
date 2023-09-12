from django.http import HttpResponse
from django.shortcuts import redirect, render


def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")


def tasks_table(request):
    return render(request, 'test.html', {})

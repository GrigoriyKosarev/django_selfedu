from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("Page app women")


def categories(request):
    return HttpResponse("<h1>Page app categories</h1>")

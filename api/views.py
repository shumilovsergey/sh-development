from django.shortcuts import render, redirect


def index(request):
    tasks = "q"
    return render(request, 'index.html')
    
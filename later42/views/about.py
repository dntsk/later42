from django.shortcuts import render


def get(request):
    return render(request, 'about.html')

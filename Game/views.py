from django.shortcuts import render

from .models import Game


# Create your views here.

def main_page(request):
    Games = Game.objects.filter(Popular=True)
    return render(request, 'main.html', {'Games': Games})


def games(request):
    Games = Game.objects.all()
    return render(request, 'games.html', {'Games': Games})


def test(request):
    Games = Game.objects.all()
    return render(request, 'test.html', {'Games': Games})


def contact(request):
    return render(request, "contact.html")


def error(request):
    return render(request, "Error.html")


def about(request):
    return render(request, 'about.html')


def nobuy(request):
    return render(request, 'nobuy.html')


def search(request):
    search = request.GET['search']
    Games = Game.objects.filter(Name__icontains=search)
    parameter = {'game': Games}
    return render(request, 'search.html', parameter)

from django.http import HttpResponse  # allows us to send a response to the user
from django.shortcuts import render


def homepage(request):

    return render(request, 'homepage.html')
    #return HttpResponse('homepage')


def about(request):

    return render(request, 'about.html')
    # return HttpResponse('about')

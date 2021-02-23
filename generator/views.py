from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here. the apps
# all the information we need is in the request form

def home(request):
    # if you want to it be a HTML
    # and the templates folder must be exactly templates
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):

    character = list("abcdefghijklmnopqrstuvwxyz")

    length = int(request.GET.get("length", 12)) # can also add a default value

    if request.GET.get('uppercase'):
        character.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    if request.GET.get("special"):
        character.extend((list("!@#$%^&*")))

    if request.GET.get("number"):
        character.extend([str(x) for x in range(10)])  # notice here x must be str


    thepassword = ""
    for x in range(length):
        thepassword += random.choice(character)


    return render(request, 'generator/password.html', {'password': thepassword})

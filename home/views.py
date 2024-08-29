from django.shortcuts import render


def home(request):
    return render(request, "home/new_index.html")


def contact(request):
    return render(request, "home/contact.html")


def symposium(request):
    return render(request, "home/symposium.html")


def who_we_are(request):
    return render(request, "home/who_we_are.html")

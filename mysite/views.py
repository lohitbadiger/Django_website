from django.shortcuts import render


def index(request):
    return render(request,'mysite/index.html')

def about(request):
    return render(request,'mysite/about.html')


def contact(request):
    return render(request,'mysite/contact.html')
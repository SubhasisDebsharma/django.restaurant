from django.shortcuts import render


def index(request):
    return render(template_name="home/index.html", request=request)
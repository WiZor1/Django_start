from django.http import HttpResponse, HttpRequest

# Create your views here.
# Все отображения в виде функций принимают один аргумент - request

def homePageView(request: HttpRequest):
    return HttpResponse('Hello Web!')
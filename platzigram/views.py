# Django
from django.http import HttpResponse, JsonResponse
from datetime import datetime

def hello_world(request):
    return HttpResponse('Hello, world!<br />Current time is {now}'.format(
        now=datetime.now().strftime('%b %d, %Y - %H:%M hrs')
    ))

def sorted(request):
    numbers:str = request.GET['numbers']
    return JsonResponse(sorted([int(i) for i in numbers.split(',')]), safe=False)

def hi(request, name, age):
    if age < 18:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello {}, welcome to platzigram'.format(name)
    return HttpResponse(message)

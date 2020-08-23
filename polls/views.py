from django.shortcuts import render
from django.http import HttpResponse
# from . models import Question

# Create your views here.
def index(request):
    return HttpResponse('"Hello, world. You are at the polls index."')

def owner(request):
    return HttpResponse("Hello, world. f15eda31 is the polls index.")

# def detail(request):
#     context = {
#         'que':Question.objects.all()
#     }
#     return render(request, 'polls/home.html', context)

from django.shortcuts import render

from .models import Topic
# Create your views here.

def index(request):
    ''' Homepage for learning_logs. '''
    return render(request, 'learning_logs/index.html')

def topics(request):
    """ . """

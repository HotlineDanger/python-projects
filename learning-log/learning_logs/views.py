from django.shortcuts import render

from .models import Topic
# Create your views here.

def index(request):
    ''' Homepage for learning_logs. '''
    return render(request, 'learning_logs/index.html')

def topics(request):
    """ Show all topics. """
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}

    return render(request, 'learning_logs/topics.html', context)
    # We first import the model associated with the data we need u. The topics() function needs one parameter: the request object Django received
    # from the server v. At w we query the database by asking for the Topic objects, sorted by the date_added attribute. We store the resulting queryset
    # in topics. At x we define a context that we’ll send to the template. A context is a dictionary in which the keys are names we’ll use in the template to access
    # the data and the values are the data we need to send to the template. In this case, there’s one key-value pair, which contains the set of topics we’ll display
    # on the page. When building a page that uses data, we pass the context variable to render() as well as the request object and the path to the template y.

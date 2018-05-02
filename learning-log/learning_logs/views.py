from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
from .forms import TopicForm, EntryForm
# Create your views here.

def index(request):
    ''' Homepage for learning_logs. '''
    return render(request, 'learning_logs/index.html')

@login_required
# We apply login_required() as a decorator to the topics() view function by prepending login_required
# with the @ symbol so Python knows to run the code in login_required() before the code in topics().
# The code in login_required() checks to see if a user is logged in, and Django will run the code in
# topics() only if they are. If the user is not logged in, they’re redirected to the login page.
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

def topic(request, topic_id):
    """ Show a single topic and all its entries. """
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set.order_by('-date_added') # - to sort in reverse order
    context = { 'topic': topic, 'entries': entries }

    return render(request, 'learning_logs/topic.html', context)
    # The function accepts the value captured by the expression (?P<topic_id>\d+) and stores it in topic_id

def new_topic(request):
    """ Add a new topic. """
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = TopicForm()
    else:
        # POST data submitted; process data
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('topics'))
            # The reverse() function determines the URL from a named URL pattern, meaning that
            # Django will generate the URL when the page is requested. We also import the form we just wrote, TopicForm.

    context = { 'form': form }
    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request, topic_id):
    """ Add a new entry for a particular topic. """
    topic = Topic.objects.get(id = topic_id)

    if request.method != 'POST':
        # No data submitted create a blank form
        form = EntryForm()
    else:
        # Post data submitted and process data
        form = EntryForm(data = request.POST)

        if form.is_valid():
            new_entry = form.save(commit = False)
            new_entry.topic = topic
            mew_entry.save()

            return HttpResponseRedirect(reverse('topic', args=[topic_id]))

    context = { 'topic': topic, 'form': form }
    return render(request, 'learning_logs/new_entry.html', context)

def edit_entry(request, entry_id):
    """ Edit an existing entry. """
    entry = Entry.objects.get(id = entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # Initial request: pre-fill form with the current entry
        form = EntryForm(instance = entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance = entry, data = request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic', args = [topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

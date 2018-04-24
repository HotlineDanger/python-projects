""" Defines URL patterns for learning_logs. """

from django.conf.urls import url, include
# from django.urls import path, include
from . import views

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),

    # Show all topics
    url(r'^topic/$', views.topics, name='topics'),

    # The r tells Python to interpret the following string as a raw string, and the quotes tell Python where the regular expression begins and ends. The caret (^) tells Python to
    # find the beginning of the string, and the dollar sign tells Python to look for the end of the string. In its entirety, this expression tells Python to look for a URL with
    # nothing between the beginning and end of the URL. Python ignores the base URL for the project (http://localhost:8000/), so an empty regular expression matches the base URL

    # Detail page for a single topic
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic')

    # Page for adding a new topic
    url(r'^new_topic/$', views.new_topic, name='new_topic')

    # The r tells Django to interpret the string as a raw string, and the expression is contained in quotes. The second part of the
    # expression, /(?P<topic_id>\d+)/, matches an integer between two forward slashes and stores the integer value in an argument called topic_id. The
    # parentheses surrounding this part of the expression captures the value stored in the URL; the ?P<topic_id> part stores the matched value in
    # topic_id; and the expression \d+ matches any number of digits that appear between the forward slashes. When Django finds a URL
]

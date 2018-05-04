from django.db import models

from django.contrib.auth.models import User

class Topic(models.Model):
    ''' A topic the user is learning about. '''
    text = models.CharField(max_length = 200) #  telling that text is a Charfield type. piece of data made up of characters. 200 characters is how much space we want it to take in the DB.
    date_added = models.DateTimeField(auto_now_add = True) # piece of data that wiull record date and time. auto_now_add set this attribute to the current date and time whenever the user creates a new topic
    owner = models.ForeignKey(User, on_delete = models.DO_NOTHING) # Connecting Data to Certain Users

    def __str__(self):
        ''' Return a string representation of the model. '''
        # tell Django which attribute to use by default when it displays
        # information about a topic. Django calls a __str__() method to display
        # a simple representation of a model. Here we’ve written a __str__() method
        # that returns the string stored in the text attribute
        return self.text

class Entry(models.Model):
    ''' Something specific we learned about the topic. '''
    topic = models.ForeignKey(Topic, on_delete = models.DO_NOTHING)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        ''' Return a string representation of the model. '''
        return self.text[:50] + '...'

'''The Entry class inherits from Django’s base Model class, just as Topic
did u. The first attribute, topic, is a ForeignKey instance v. A foreign key is a
database term; it’s a reference to another record in the database. This is the
code that connects each entry to a specific topic. Each topic is assigned a
key, or ID, when it’s created. When Django needs to establish a connection
between two pieces of data, it uses the key associated with each piece of
information. We’ll use these connections shortly to retrieve all the entries
associated with a certain topic.
Next is an attribute called text, which is an instance of TextField w.
This kind of field doesn’t need a size limit, because we don’t want to limit
the size of individual entries. The date_added attribute allows us to present
entries in the order they were created and to place a timestamp next to
each entry.
At x we nest the Meta class inside our Entry class. Meta holds extra information
telling Django to use Entries when it needs to refer to more than one entry.
for managing a model; here it allows us to set a special attribute
(Without this, Django would refer to multiple entries as Entrys.) Finally,
the __str__() method tells Django which information to show when it refers
to individual entries. Because an entry can be a long body of text, we tell
Django to show just the first 50 characters of text y. We also add an ellipsis
to clarify that we’re not always displaying the entire entry.
'''

from django.db import models

class Topic(models.Model):
    """ A topic the user is learning about. """
    text = models.CharField(max_length = 200) #  telling that text is a Charfield type. piece of data made up of characters. 200 characters is how much space we want it to take in the DB.
    date_added = models.DateTimeField(auto_now_add = True) # piece of data that wiull record date and time. auto_now_add set this attribute to the current date and time whenever the user creates a new topic

    def __str__(self):
        """ Return a string representation of the model. """
        # tell Django which attribute to use by default when it displays
        # information about a topic. Django calls a __str__() method to display
        # a simple representation of a model. Here we’ve written a __str__() method
        # that returns the string stored in the text attribute
        return self.text

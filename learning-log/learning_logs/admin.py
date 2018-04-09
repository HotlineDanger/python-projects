from django.contrib import admin

from learning_logs.models import Topic, Entry


'''This code imports the model we want to register, Topic u, and then uses
admin.site.register() v to tell Django to manage our model through the
admin site.'''

admin.site.register(Topic)
admin.site.register(Entry)

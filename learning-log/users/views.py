from django.http impot HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout
from django.shortcuts import render

def logout_view(request):
    """ Log the user out. """
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

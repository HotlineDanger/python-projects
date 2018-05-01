from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout
from django.shortcuts import render

def logout_view(request):
    """ Log the user out. """
    logout(request)
    return HttpResponseRedirect(reverse('index'))

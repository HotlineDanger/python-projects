"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(r'^admin/', include(admin.site.urls)),
    path(r'', include('learning_logs.urls', namespace='learning_logs')),
]

"""
Namespace argument allows us to distinguish
learning_logs’s URLs from other URLs that might appear in the project,
which can be very helpful as your project starts to grow.
The default urls.py is in the learning_log folder; now we need to make a
second urls.py file in the learning_logs folder:
"""

"""
URL configuration for travelblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from travelapp.views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name='index'),
    path('blog/',blog,name='blog'),
    path('blog/<int:pk>/', postdetails,name='posts'),
    path('aboutme/',aboutme,name='aboutme'),
    path('projects/',projects,name='projects'),
    path('certifications/',certifications,name='certifications'),
    path('contacts/',contacts,name='contacts'),
    path('explore/',explore,name='explore'),
    path('myskills/',myskills,name='myskills'),

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

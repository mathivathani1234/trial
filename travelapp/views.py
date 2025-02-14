from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .models import Video 
# Create your views here.
def index(request):
    return render(request,'index.html')
def blog(request):
    postlist = Post.objects.all()
    return render(request,'blog.html',{'postlist':postlist})

def postdetails(request,pk):
    postlist = Post.objects.get(pk=pk)
    return render(request, 'postdetails.html', {'postlist':postlist})

def aboutme(request):
    return render(request,'aboutme.html')

def projects(request):
    return render(request,'projects.html')

def certifications(request):
    return render(request,'certifications.html')

def contacts(request):
    return render(request,'contact.html')

def explore(request):
    video=Video.objects.all()
    return render(request,'explore.html',{"video":video})

def myskills(request):
    return render(request,'myskills.html')
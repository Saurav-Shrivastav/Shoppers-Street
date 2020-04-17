from django.shortcuts import render
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'store/home.html', context)

def about(request):
    return render(request, 'store/about.html', { 'title': 'About'})

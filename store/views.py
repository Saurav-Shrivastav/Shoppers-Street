from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required

def dashboard(request):
    return render(request, 'store/dashboard.html')

@login_required
def home(request):
    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'store/home.html', context)

def about(request):
    return render(request, 'store/about.html', { 'title': 'About'})

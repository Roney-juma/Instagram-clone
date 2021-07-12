from django.shortcuts import render
from .models import Post, Username

# Create your views here.
def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'photo/home.html', context)
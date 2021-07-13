from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Username

# Create your views here.
def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'photo/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'photo/home.html'
    context_object_name = 'posts'
    ordering  = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
    template_name = 'photo/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image',]
    template_name="photo/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
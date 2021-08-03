
from django.shortcuts import render
from .models import post
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

# Create your views here.


def home(request):
    context = {
        'posts': post.objects.all()
    }
    
    return render(request, 'chatblog/home.html',context)

    

class PostListView(ListView):
    model=post
    template_name='chatblog/home.html'
    context_object_name='posts'
    ordering=['date_posted']
    

class PostDetailView(DetailView):
    model=post

class PostCreatView(LoginRequiredMixin,CreateView):
    model=post
    success_url = '/'
    fields=['content']
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = post
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'chatblog/about.html')

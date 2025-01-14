from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView, ListView, DetailView, FormView, CreateView, UpdateView, \
    DeleteView

from .forms import PostForm
from .models import Post


def index_view(request):
    return render(request, 'index.html')

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Django'
        context['posts'] = Post.objects.all()
        return context

class RedirectToMaktab(RedirectView):
    url = 'https://maktabkhooneh.org'


class PostList(PermissionRequiredMixin,LoginRequiredMixin,ListView):
    permission_required = 'blog.view_post'
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 2
    ordering = ['-created_at']
    queryset = Post.objects.filter(status=True)

class PostDetail(DetailView):
    model = Post
    context_object_name = 'post'
    queryset = Post.objects.filter(status=True)

'''
class PostCreateView(FormView):
    form_class = PostForm

    template_name = 'contact.html'
    success_url = '/blog/posts/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

'''

class PostCreateView(CreateView ):
    model = Post
    # fields = ['title', 'author', 'content', 'category', 'published_at', 'status']
    form_class = PostForm
    success_url = '/blog/posts/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostEditView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/posts/'

class PostDeleteView(DeleteView):
    model = Post
    success_url = '/blog/posts/'
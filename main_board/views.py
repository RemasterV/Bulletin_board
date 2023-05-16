from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Post, Message
from .forms import PostForm, MessageForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class Posts(ListView):
    model = Post
    ordering = 'title'
    template_name = 'posts.html'
    context_object_name = 'posts'



class OnePost(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

class PostCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('main_board.add_post')
    raise_exception = True
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'
    success_url = reverse_lazy('main')


class PostEdit(PermissionRequiredMixin, UpdateView):
    permission_required = ('main_board.change_post')
    raise_exception = True
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    success_url = reverse_lazy('main')

class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('main_board.delete_post')
    raise_exception = True
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('main')

class MessageCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = MessageForm
    model = Message
    template_name = 'message_create.html'
    success_url = reverse_lazy('main')


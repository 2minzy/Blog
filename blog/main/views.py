from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone
from django.shortcuts import get_object_or_404
from login.models import Account
# Create your views here.

def home(request):
  post = Post.objects.all()
  context = {'post': post }
  if request.user.is_authenticated:
    now_login = Account.objects.get(user = request.user)
    context = {'post':post,'user':now_login}
  return render(request,'home.html', context)

def post(request):
  if request.method == 'POST':
    new_post = Post()
    title = request.POST.get('title')
    content = request.POST.get('content')
    new_post.title = title
    new_post.content = content
    new_post.pub_date = timezone.datetime.now()
    new_post.save()
  return render(request, 'post.html')

def detail(request, post_id):
  post = get_object_or_404(Post,pk = post_id)
  context = {'post' : post}
  return render(request,'detail.html', context)

def update_post(request, post_id):
  post_update = Post.objects.get(id = post_id)
  context = {'post':post_update}
  if request.method == "POST":
    title = request.POST.get('title')
    content = request.POST.get('content')
    post_update.title = title
    post_update.content = content
    post_update.pub_date = timezone.datetime.now()
    post_update.save()
    context = {"post": post_update}
    return render(request, 'detail.html', context)
  return render(request,'post.html', context)

def delete_post(request, post_id):
  post_delete = Post.objects.get(id=post_id)
  post_delete.delete()
  return redirect('home')




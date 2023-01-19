from django.shortcuts import render,get_object_or_404
from .models import Post
from django.views.generic import ListView,DetailView
# Create your views here.

def post_list(request):
    all_post = Post.objects.all()
    context = {'all_post':all_post}
    return render(request,'blog/post_list.html',context)    

def post_detail(request,id):
    post = get_object_or_404(Post,id=id)
    return render(request,'blog/post_detail.html',{'post':post})

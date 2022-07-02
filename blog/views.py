from django.shortcuts import render
from.models import Post
# Create your views here.


def post_list(request):
    all_post= Post.objects.all()
    context ={'posts':all_post}
    return render(request,'blog/post_list.html',context)

def post_detail(request,id):
    post=Post.objects.get(id=id)
    return render(request,'blog/post_detail.html',{'post':post})

from django.shortcuts import render,redirect
from.models import Post
from.forms import PostForm

# Create your views here.


def post_list(request):
    all_post= Post.objects.all()
    context ={'posts':all_post}
    return render(request,'blog/post_list.html',context)

def post_detail(request,id):
    post=Post.objects.get(id=id)
    return render(request,'blog/post_detail.html',{'post':post})

def new_post(request):
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()
    return render(request,'blog/new_post.html',{'form':form})
    

def edit_post(request,id):
    post=Post.objects.get(id=id)
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
    else:
        form = PostForm(instance=post)
    return render(request,'blog/new_post.html',{'form':form})

def delete_post(request,id):
    post=Post.objects.get(id=id)
    post.delete()
    return redirect('/blog')


from django.views.generic import ListView,DetailView,DeleteView

class PostList(ListView):
    model = Post

class PostDetail(DetailView):
    model = Post

class PostDelete(DeleteView):
    model = Post
    success_url = '/blog'
from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from .forms import PostForm
# Create your views here.


# Function

def post_list(request):
    all_post = Post.objects.all()
    context = {'all_post':all_post}
    return render(request,'blog/post_list.html',context)    

def post_detail(request,id):
    post = get_object_or_404(Post,id=id)
    return render(request,'blog/post_detail.html',{'post':post})


def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()
    return render(request,'blog/new_post.html',{'form':form})

def edit_post(request,id):
    post =get_object_or_404(Post,id=id)
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = PostForm(instance=post)
    return render(request,'blog/new_post.html',{'form':form})

def delete_post(request,id):
    post = get_object_or_404(Post,id=id)
    post.delete()
    return redirect('/blog')



# class based view

from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

class PostList(ListView):
    model=Post

class PostDetail(DetailView):
    model = Post

class PostDelete(DeleteView):
    model = Post
    success_url ='/blog/cbv'

class PostEdit(UpdateView):
    model = Post
    fields = '__all__'
    template_name='blog/new_post.html'

class PostNew(CreateView):
    model = Post
    fields = '__all__'
    template_name='blog/new_post.html'
    # success_url ='/blog/cbv'
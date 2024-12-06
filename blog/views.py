from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Author
from .forms import PostForm, AuthorForm

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def posts(request):
    postss = Post.objects.all().order_by('-published_date')
    return render(request, 'blog/posts.html', {'posts': postss})

def create_posts(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts')
        else:
            return redirect('home')
        
    form = PostForm()
    context = {'form': form}
    return render(request, 'blog/create_posts.html', context)

def edit_post(request, item_id):
    item = get_object_or_404(Post, id=item_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            item.name = form.cleaned_data['title']
            item.content = form.cleaned_data['content']
            item.image = form.cleaned_data['image']
            item.author = form.cleaned_data['author']
            item.save()
        return redirect('posts')
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'blog/edit_post.html', {'form': form, 'item': item})
    
def show_det_post(request, item_id):
    postss = get_object_or_404(Post, id=item_id)
    return render(request, 'blog/post_detail.html', {'posts': postss})

def show_det_author(request, item_id):
    author = get_object_or_404(Author, id=item_id)
    postss = Post.objects.filter(author=author)
    return render(request, 'blog/post_by_author.html', {'posts': postss, 'author': author})

def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')
        else:
            return redirect('home')
        
    form = AuthorForm()
    context = {'form': form}
    return render(request, 'blog/create_author.html', context)
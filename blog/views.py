from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.objects.order_by('created_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_tag(request, tag):
    posts = Post.objects.order_by('created_date').filter(add_tags=tag)  #(Post('tags_add')==request.GET)
    return render(request, 'blog/post_list.html', {'posts': posts})
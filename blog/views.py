from django.shortcuts import render, get_object_or_404
from .models import Post
from .models import Tag
from django.http import HttpResponse

def post_list(request):
    posts = Post.objects.order_by('created_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_tag(request, tag):
    received_tag = Tag.objects.filter(slug = tag)
    posts = Post.objects.order_by('created_date').filter(add_tags = received_tag)  #(Post('tags_add')==request.GET)
    return render(request, 'blog/post_list.html', {'posts': posts})
#    return HttpResponse(tag)

#def tag (request, id): # тут все тоже самое
#    tag = Tag.objects.select_related().get(id=id)
#    posts = tag.post_set.all()
#    return render(request, 'blog/post_list.html', {'posts': posts, 'tag': tag}
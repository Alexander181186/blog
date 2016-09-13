from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from .models import Tag

def pagination_posts(request, posts_list, n_posts):
    paginator = Paginator(posts_list, n_posts)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)    
    return posts


def post_list(request):
    posts_list = Post.objects.all().order_by('created_date')
    posts = pagination_posts(request, posts_list, 10)
    return render_to_response('blog/post_list.html', {'posts': posts})
    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_tag(request, tag):
    received_tag = Tag.objects.filter(slug = tag)
    posts_list = Post.objects.order_by('created_date').filter(add_tags = received_tag)  #(Post('tags_add')==request.GET)
    posts = pagination_posts(request, posts_list, 10)
    return render_to_response('blog/post_list.html', {'posts': posts})
#    return HttpResponse(tag)

#def tag (request, id): # тут все тоже самое
#    tag = Tag.objects.select_related().get(id=id)
#    posts = tag.post_set.all()
#    return render(request, 'blog/post_list.html', {'posts': posts, 'tag': tag}
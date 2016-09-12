from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^tag/(\w+)/$', views.post_tag, name='post_tag'),
 #   url(r'^tag/(?P<id>\d+)/$', 'tag'),
]



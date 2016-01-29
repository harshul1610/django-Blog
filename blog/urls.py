from django.conf.urls import url
import views

urlpatterns = [
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.edit_post, name='post_edit'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^$', views.post_list, name='post_list'),
]
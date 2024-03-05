from django.urls import path
from . import views

urlpatterns =[
    path("",views.index, name="home"),
    path("posts", views.posts, name="posts-page"),
    path("posts/<slug:slug>",views.post, name="post-detail-page") #/posts/my-first-post
]
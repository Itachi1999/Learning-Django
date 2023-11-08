from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.starting_page, name='starting_page'),
    path("posts", view=views.posts, name='posts_page'),
    path("posts/<slug:slug>", view=views.post_details, name='post_detail_page'),
]


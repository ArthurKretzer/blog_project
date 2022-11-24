from django.urls import path
from . import views

urlpatterns = [
    # this configures a place holder named month to dynamically set the route. We specify the type for the input. In that way we can set different routes.
    path("", views.starting_page, name="starting-page"),
    path("posts", views.posts, name="posts-page"),
    path("posts/<slug>", views.post_detail, name="posts-detail-page"), # /posts/my-first-post
]

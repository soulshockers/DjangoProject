from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path("", views.home, name="home"),
    path("categories/", views.category_list, name="category_list"),
    path("categories/<int:category_id>/", views.category_detail, name="category_detail"),
    path("categories/add/", views.category_add, name="category_add"),
    path("categories/<int:category_id>/edit/", views.category_edit, name="category_edit"),

    path("posts/<int:post_id>/", views.post_detail, name="post_detail"),
    path("posts/add/<int:category_id>/", views.post_add, name="post_add"),
    path("posts/<int:post_id>/edit", views.post_edit, name="post_edit"),
]
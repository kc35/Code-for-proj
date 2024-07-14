
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("category/<category>/", views.blog_category, name="blog_category"),
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),
]

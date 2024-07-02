from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("mailing/", include("mailing.urls", namespace="mailing")),
    path("", include("client.urls", namespace="client")),
    path("users/", include("users.urls", namespace="users")),
    path("blog/", include("blog.urls", namespace="blog")),
]

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import never_cache, cache_page

from blog.apps import BlogConfig
from blog.views import (
    BlogListView,
    BlogDetailsView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)

app_name = BlogConfig.name

urlpatterns = [
    path("posts/", cache_page(60)(BlogListView.as_view(template_name="blogs/blog_list.html")), name="post_list"),
    path("post/<int:pk>/", BlogDetailsView.as_view(template_name="blogs/blog_detail.html"), name="post_detail"),
    path("post/create/", never_cache(BlogCreateView.as_view(template_name="blogs/blog_form.html")), name="post_create"),
    path(
        "post/<int:pk>/update/",
        never_cache(BlogUpdateView.as_view()),
        name="post_update",
    ),
    path(
        "post/<int:pk>/delete/",
        never_cache(BlogDeleteView.as_view(template_name="blogs/blog_confirm_delete.html")),
        name="post_delete",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

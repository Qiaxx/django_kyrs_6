from django.shortcuts import render


from django.template.defaultfilters import slugify
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from blog.models import Blog


class BlogListView(ListView):
    model = Blog


class BlogDetailsView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blog
    fields = ("title", "slug", "content", "preview", "published", "views_count")
    success_url = reverse_lazy("catalog:post_list")

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.slug = slugify(new_post.title)
            new_post.save()
            return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ("title", "slug", "content", "preview", "published", "views_count")
    success_url = reverse_lazy("catalog:post_list")

    def get_success_url(self):
        return reverse("catalog:post_detail", args=[self.kwargs.get("pk")])


class BlogDeleteView(DeleteView):
    model = Blog
from django.db import models


from django.db import models
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField(
        max_length=100, verbose_name="Заголовок", help_text="Введите заголовок"
    )
    slug = models.SlugField(unique=True, blank=True, null=True)
    content = models.TextField(verbose_name="Текст", help_text="Введите текст")
    preview = models.ImageField(
        upload_to="blog_previews",
        verbose_name="Изображение",
        help_text="Вставьте изображение",
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    published = models.BooleanField(default=False, verbose_name="Опубликовано")
    views_count = models.PositiveIntegerField(
        default=0,
        verbose_name="Количество просмотров",
        help_text="Введите количество просмотров",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Статья блога"
        verbose_name_plural = "Статьи блога"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"slug": self.slug})

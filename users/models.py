from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="почта")
    first_name = models.CharField(max_length=15, verbose_name="Имя")
    last_name = models.CharField(max_length=30, verbose_name="Фамилия")
    is_blocked = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        permissions = [
            ("block_user", "Can blocking users"),
        ]

    def __str__(self):
        return self.email

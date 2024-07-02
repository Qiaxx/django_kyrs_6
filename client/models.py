from django.db import models

from users.models import User


class Client(models.Model):
    full_name = models.CharField(
        max_length=255, verbose_name="Ф.И.О клиента", help_text="Введите Ф.И.О клиента"
    )
    email = models.EmailField(
        unique=True, verbose_name="E-mail клиента", help_text="Введите E-mail клиента"
    )
    comment = models.TextField(
        blank=True,
        null=True,
        verbose_name="Комментарий клиента",
        help_text="Введите комментарий клиента",
    )
    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        help_text="Укажите владельца товара",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return f"{self.full_name} ({self.email})"

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

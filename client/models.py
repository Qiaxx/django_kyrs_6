from django.db import models


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

    def __str__(self):
        return f"{self.full_name} ({self.email})"

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

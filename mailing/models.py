from django.db import models

from client.models import Client


class Message(models.Model):
    subject = models.CharField(
        max_length=255, verbose_name="Тема сообщения", help_text="Введите тему"
    )
    body = models.TextField(
        verbose_name="Текст сообщения", help_text="Введите текст сообщения"
    )

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"


class Mailing(models.Model):
    STATUS_CHOICES = [
        ("created", "Created"),
        ("started", "Started"),
        ("completed", "Completed"),
    ]
    start_datetime = models.DateTimeField()
    frequency = models.CharField(
        max_length=10,
        choices=[("daily", "Daily"), ("weekly", "Weekly"), ("monthly", "Monthly")],
        verbose_name="Частота рассылки",
        default="daily",
        help_text="Выберите частоту рассылки",
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="created",
        verbose_name="Статус рассылки",
        help_text="Выберите статус рассылки",
    )
    message = models.OneToOneField(Message, on_delete=models.CASCADE)
    clients = models.ManyToManyField(Client)

    def __str__(self):
        return f"Рассылка {self.id} - {self.status}"

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"


class Attempt(models.Model):
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE)
    attempt_datetime = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата и время попытки"
    )
    status = models.CharField(
        max_length=10,
        choices=[("success", "Success"), ("failure", "Failure")],
        verbose_name="Статус попытки",
    )
    server_response = models.TextField(
        blank=True, null=True, verbose_name="Ответ сервера"
    )

    def __str__(self):
        return f"Попытка {self.id} - {self.status}"

    class Meta:
        verbose_name = "Попытка"
        verbose_name_plural = "Попытки"

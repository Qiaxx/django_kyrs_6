from django.contrib import admin

from client.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "email", "comment")
    list_filter = (
        "full_name",
        "email",
    )
    search_fields = (
        "full_name",
        "email",
    )

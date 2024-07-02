from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email")
    list_filter = ("email",)
    search_fields = ("id", "email")

    def block_users(self, request, queryset):
        queryset.update(is_blocked=True)

    block_users.short_description = "Block selected users"

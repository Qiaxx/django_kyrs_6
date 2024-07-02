from django.contrib import admin


from mailing.models import Message, Mailing


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "subject")
    list_filter = (
        "subject",
    )
    search_fields = (
        "subject",
    )


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ['status', "message"]
    actions = ['deactivate_mailings']

    def deactivate_mailings(self, request, queryset):
        queryset.update(is_active=False)
    deactivate_mailings.short_description = "Deactivate selected mailings"

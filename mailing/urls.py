from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from mailing import views
from mailing.apps import MailingConfig
from mailing.views import MessageCreateView, MessageListView, MessageDetailsView, MessageUpdateView, MessageDeleteView

app_name = MailingConfig.name

urlpatterns = [
    path("message_create/", MessageCreateView.as_view(), name="message_create"),
    path("message_list/", MessageListView.as_view(), name="message_list"),
    path("message_detail/<int:pk>/", MessageDetailsView.as_view(), name="message_detail"),
    path("message_update/<int:pk>/", MessageUpdateView.as_view(), name="message_update"),
    path("message_delete/<int:pk>/", MessageDeleteView.as_view(), name="message_delete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

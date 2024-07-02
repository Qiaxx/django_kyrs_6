from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page

from client.apps import ClientConfig
from client.views import ClientListView, ClientDetailsView
from mailing import views

app_name = ClientConfig.name

urlpatterns = [
    path("", cache_page(60)(views.base), name="home"),
    path("clients/", ClientListView.as_view(), name="client_list"),
    path("client/<int:pk>/", ClientDetailsView.as_view(), name="client_detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.core.cache import cache

from config.settings import CACHE_ENABLED
from mailing.models import Message


def get_cached_messages():
    """
    Получение списка категорий из кэша. В случае, если кэш пустой, берет данные из БД.
    """
    if not CACHE_ENABLED:
        return Message.objects.all()
    messages = cache.get("messages")
    if not messages:
        categories = Message.objects.all()
        cache.set("messages", categories, 60 * 15)  # Кэшируем на 15 минут
    return messages

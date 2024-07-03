from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from mailing.models import Message


from blog.models import Blog
from mailing.models import Mailing
from mailing.services import get_cached_messages
from users.models import User


def base(request):
    total_mailings = Mailing.objects.count()
    active_mailings = Mailing.objects.filter(is_active=True).count()
    unique_clients = User.objects.distinct().count()
    random_blog_posts = Blog.objects.order_by('?')[:3]

    context = {
        'total_mailings': total_mailings,
        'active_mailings': active_mailings,
        'unique_clients': unique_clients,
        'random_blog_posts': random_blog_posts,
    }

    return render(request, 'mailing/first.html', context)


class MessageListView(ListView):
    model = Message
    context_object_name = "messages"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["messages"] = Message.objects.all()

        return context

    def get_queryset(self):
        return get_cached_messages()


class MessageDetailsView(DetailView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
    fields = ("subject", "body")
    success_url = reverse_lazy("mailing:message_list")

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.user = user
        product.save()
        return super().form_valid(form)


class MessageUpdateView(UpdateView):
    model = Message
    fields = ("subject", "body")

    def get_success_url(self):
        return reverse("mailing:message_detail", kwargs={"pk": self.object.pk})


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy("mailing:message_list")
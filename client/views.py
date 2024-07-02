from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from client.models import Client


class ClientListView(ListView):
    model = Client


class ClientDetailsView(DetailView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    fields = ("full_name", "email", "comment")
    success_url = reverse_lazy("client:client_list")

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.user = user
        product.save()
        return super().form_valid(form)


class ClientUpdateView(UpdateView):
    model = Client
    fields = ("full_name", "email", "comment")

    def get_success_url(self):
        return reverse("client:client_detail", args=[self.kwargs.get("pk")])


class ClientDeleteView(DeleteView):
    model = Client

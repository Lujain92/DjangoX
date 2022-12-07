from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Country


class CountryListView(ListView):
    template_name = "country/country_list.html"
    model = Country


class CountryDetailView(DetailView):
    template_name = "country/country_detail.html"
    model = Country


class CountryCreateView(CreateView):
    template_name = "country/country_create.html"
    model = Country
    fields = ['name','author','desc']


class CountryUpdateView(UpdateView):
    template_name = "country/country_update.html"
    model = Country
    fields = ['name','author','desc']


class CountryDeleteView(DeleteView):
    template_name = "country/country_delete.html"
    model = Country
    success_url = reverse_lazy("country_list")
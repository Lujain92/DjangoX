from django.urls import path
from .views import CountryListView, CountryDetailView, CountryCreateView, CountryUpdateView, CountryDeleteView

urlpatterns = [
    path('country/', CountryListView.as_view(), name='country_list'),
    path('country/<int:pk>/', CountryDetailView.as_view(), name='country_detail'),
    path('country/create/', CountryCreateView.as_view(), name='country_create'),
    path('country/<int:pk>/update/', CountryUpdateView.as_view(), name='country_update'),
    path('country/<int:pk>/delete/', CountryDeleteView.as_view(), name='country_delete'),
]
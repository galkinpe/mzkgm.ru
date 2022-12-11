from django.urls import path
from django.views.decorators.cache import cache_page
from .views import *

urlpatterns = [
    path("", cache_page(60)(HomeView.as_view()), name="home"),
    path("news/", cache_page(60)(NewsView.as_view()), name="news"),
    path("doctors/", cache_page(60)(DoctorsView.as_view()), name="doctors"),
    path("doctors/<int:pk>/", DoctorDetailView.as_view(), name="doctor"),
    path("contacts/", get_contacts, name="contacts"),
    path("news/<int:pk>/", cache_page(60)(NewsDetailView.as_view()), name="news_detail"),
    path("about/", about, name="about"),
    path("price/", cache_page(60)(PriceView.as_view()), name="price"),
    path("price/<str:slug>", GetService.as_view(), name="price_detail"),
    path("directions/", cache_page(60)(DirectionsView.as_view()), name="directions"),
    path("directions/<str:slug>", cache_page(60)(DirectionsDetailView.as_view()), name="direction"),
    path("prepare/", prepare, name="prepare"),

]

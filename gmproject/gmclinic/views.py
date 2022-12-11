from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView
from .models import *


# Create your views here.


# def index(request):
#     return render(request, 'index.html')

class HomeView(ListView):
    """Врачи и новости на главной странице"""
    Model = Doctor
    template_name = 'gm/index.html'
    context_object_name = 'doctors'
    queryset = Doctor.objects.all()

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data()
        context['news'] = News.objects.all()
        return context


class NewsView(ListView):
    """Новости"""
    Model = News
    template_name = 'gm/news.html'
    context_object_name = 'news'
    queryset = News.objects.filter(is_published=True)


class NewsDetailView(DetailView):
    """Отдельно выбранная новость"""
    model = News
    template_name = 'gm/news_detail.html'
    context_object_name = 'news'
    pk_url_kwarg = 'pk'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data()
        context['news_all'] = News.objects.all()
        return context


class DoctorsView(ListView):
    """Вывод списка всех врачей"""
    Model = Doctor
    template_name = 'gm/doctors.html'
    context_object_name = 'doctors'
    queryset = Doctor.objects.all()


class DoctorDetailView(DetailView):
    """Вывод подробной информации о враче"""
    model = Doctor
    template_name = 'gm/doctor.html'
    context_object_name = 'doctor'
    pk_url_kwarg = 'pk'
    allow_empty = False


def get_contacts(request):
    """Контакты клиники"""
    template_name = 'gm/contacts.html'
    return render(request, 'gm/contacts.html')


def about(request):
    """О клинике"""
    template_name = 'gm/about.html'
    return render(request, 'gm/about.html')


class DirectionsView(ListView):
    """Направления клиники"""
    model = Directions
    template_name = 'gm/directions.html'
    context_object_name = 'directions'
    queryset = Directions.objects.all()


class DirectionsDetailView(DetailView):
    """Подробно о выбранном направлении"""
    model = Directions
    template_name = 'gm/direction_detail.html'
    context_object_name = 'direction'
    allow_empty = False


class PriceView(ListView):
    """Прайс по категориям"""
    Model = PriceCategory
    template_name = 'gm/price.html'
    context_object_name = 'price'
    queryset = PriceCategory.objects.all()


class GetService(DetailView):
    """Прайс по выбранной категории"""
    model = PriceCategory
    template_name = 'gm/price_detail.html'
    context_object_name = 'price'
    allow_empty = False


def prepare(request):
    """Правила подготовки к диагностическим исследованиям"""
    data = Files.objects.all()
    return render(request, 'gm/prepare.html', {'data': data})

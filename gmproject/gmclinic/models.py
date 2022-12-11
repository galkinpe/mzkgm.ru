from django.db import models
from django.urls import reverse


# Create your models here.


class Doctor(models.Model):
    """Врачи"""
    title = models.CharField('Фамилия Имя Отчество', max_length=150)
    shortdescription = models.TextField('Краткое описание')
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='img/doctor/')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    draft = models.BooleanField('Опубликовано?', default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("doctor", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'Врача'
        verbose_name_plural = 'Врачи'


class News(models.Model):
    """Новости и Акции"""
    title = models.CharField('Заголовок', max_length=150)
    content = models.TextField('Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='img/news/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано?')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news_detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Directions(models.Model):
    """Направления"""
    title = models.CharField('Наименование', max_length=150)
    content = models.TextField('Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    icon = models.ImageField(upload_to='img/icon/', verbose_name='Иконка', blank=True)
    image = models.ImageField(upload_to='img/directions/', verbose_name='Изображение', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано?')
    slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("direction", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'
        ordering = ['-created_at']


class PriceCategory(models.Model):
    """Прейскурант"""
    title = models.CharField('Наименование', max_length=150)
    content = models.TextField('Описание')
    icon = models.ImageField(upload_to='img/icon/', verbose_name='Иконка', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано?')
    slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("price_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Прейскурант'
        verbose_name_plural = 'Прейскурант'
        ordering = ['-created_at']


class Files(models.Model):
    """Файлы для пациента"""
    title = models.CharField('Наименование', max_length=150)
    file = models.FileField('Файл', upload_to='uploads/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'

from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import CatDoctors, Doctor, News, Directions, PriceCategory, Files
from django import forms

# Register your models here.


from ckeditor_uploader.widgets import CKEditorUploadingWidget


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(label='Контент', widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class DoctorAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Doctor
        fields = '__all__'


class DirectionAdminForm(forms.ModelForm):
    content = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Directions
        fields = '__all__'


class PriceAdminForm(forms.ModelForm):
    content = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = PriceCategory
        fields = '__all__'


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    save_as = True
    save_on_top = True
    list_display = ('title', 'shortdescription', 'created_at', 'updated_at', 'draft', 'get_photo')
    list_display_links = ('title', 'shortdescription')
    search_fields = ('title', 'shortdescription')
    list_editable = ('draft',)
    form = DoctorAdminForm
    readonly_fields = ('created_at', 'get_photo')

    def get_photo(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="75">')

    get_photo.short_description = "Фото"


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    save_as = True
    save_on_top = True
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    form = NewsAdminForm


@admin.register(Directions)
class DirectionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    save_as = True
    save_on_top = True
    list_display = ('title', 'created_at', 'updated_at', 'is_published', 'get_icon')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_editable = ('is_published',)
    form = DirectionAdminForm
    readonly_fields = ('created_at', 'get_icon')

    def get_icon(self, obj):
        if obj.icon:
            return mark_safe(f'<img src="{obj.icon.url}" width="75">')

    get_icon.short_description = "Изображение"


@admin.register(PriceCategory)
class PriceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    save_as = True
    save_on_top = True
    list_display = ('title', 'created_at', 'updated_at', 'is_published', 'get_icon')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_editable = ('is_published',)
    form = PriceAdminForm
    readonly_fields = ('created_at', 'get_icon')

    def get_icon(self, obj):
        if obj.icon:
            return mark_safe(f'<img src="{obj.icon.url}" width="75">')

    get_icon.short_description = "Изображение"


admin.site.site_title = "GMClinic Administration"
admin.site.site_header = "GMClinic Administration"


@admin.register(Files)
class FilesAdmin(admin.ModelAdmin):
    save_as = True
    save_on_top = True

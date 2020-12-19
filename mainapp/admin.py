from django.contrib import admin
from django.forms import ModelChoiceField, ModelForm, ValidationError
from django.utils.safestring import mark_safe

from .models import *

from PIL import Image


class NotebookAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = mark_safe(
            '<span style="color: red; font-size: 14px;">Загружайте изображение с разрешением от {}x{} до {}x{}</span>'.format(
                *Product.MIN_RESOLUTION, *Product.MAX_RESOLUTION
            )
        )

    def clean_image(self):
        image = self.cleaned_data['image']
        img = Image.open(image)
        min_width, min_height = Product.MIN_RESOLUTION
        max_width, max_height = Product.MAX_RESOLUTION
        max_image_size = Product.MAX_IMAGE_SIZE
        if img.width < min_width or img.height < min_height:
            raise ValidationError('Разрешение изображения меньше минимального!')
        if img.width > max_width or img.height > max_height:
            raise ValidationError('Разрешение изображения больше максимального!')
        if image.size > max_image_size:
            raise ValidationError('Размер изображение не должен превышать 3MB!')
        return image


@admin.register(Notebook)
class NotebookAdmin(admin.ModelAdmin):

    form = NotebookAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            return ModelChoiceField(Category.objects.filter(slug="notebooks"))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Smartphone)
class SmartphoneAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            return ModelChoiceField(Category.objects.filter(slug="smartphones"))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(CartProduct)
admin.site.register(Cart)

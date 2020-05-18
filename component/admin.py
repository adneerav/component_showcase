from django.contrib import admin

# Register your models here.
from component.models import Component, Detail, DetailImage

admin.site.register(Component)


class ComponentDetailAdmin(admin.ModelAdmin):
    model = Detail
    list_display = ['component', 'get_technologies', 'get_languages']

    def get_name(self, obj):
        return obj.component.name


admin.site.register(Detail, ComponentDetailAdmin)


class ComponentImageAdmin(admin.ModelAdmin):
    model = DetailImage
    list_display = ['component_detail_image', 'image_tag']


admin.site.register(DetailImage, ComponentImageAdmin)

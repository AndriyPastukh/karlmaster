from django.contrib import admin
from index.models import *
from django.utils.safestring import mark_safe


admin.site.register(Testimonials)



@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['image_show','is_available']

    def image_show(self, obj):
        if obj.img:
            return mark_safe("<img src='{}' width='600px' />".format(obj.img.url))
        else:
            return "None"    
    image_show.__name__ = 'Picture'
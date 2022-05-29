from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from products.models import *
from django.utils.safestring import mark_safe









@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['price', 'name', 'is_available', 'feedback']
    prepopulated_fields = {'slug' : ('name',)}
    # def image_show(self, obj):
    #     if obj.images:
    #         return mark_safe("<img src='{}' width='600px' />".format(obj[0].images.url))
    #     else:
    #         return "None"    
    # image_show.__name__ = 'Picture'


@admin.register(ProductImages)
class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ['name', 'image_show']
    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='600px' />".format(obj.image.url))
        else:
            return "None"    
    image_show.__name__ = 'Picture'



# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['clothes_size']

# admin.site.register()

admin.site.register(Size)


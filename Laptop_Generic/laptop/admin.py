from django.contrib import admin
from .models import LaptopModel



class LaptopModelAdmin(admin.ModelAdmin):
    list_display=['id','laptopname','laptopCompany','laptopram','laptoprom','laptopprice','laptopprocessor']
admin.site.register(LaptopModel,LaptopModelAdmin)
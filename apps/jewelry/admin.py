from django.contrib import admin
from .models import Jewelry,JewelryType
# Register your models here.

@admin.register(Jewelry)
class JewelryAdmin(admin.ModelAdmin):
    list_display = ("id","title","author","read_num","created_time")
    list_per_page = 10


@admin.register(JewelryType)
class JewelryType(admin.ModelAdmin):
    list_display = ("id","jewelry_type")



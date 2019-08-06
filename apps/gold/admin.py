from django.contrib import admin
from .models import GoldType,GoldCollege
# Register your models here.

@admin.register(GoldType)
class GoldTypeAdmin(admin.ModelAdmin):
    list_display = ("id","gold_type")
    list_per_page = 10

@admin.register(GoldCollege)
class GoldCollegeAdmin(admin.ModelAdmin):
    list_display = ("id","title","gold_type","author","read_num","created_time")
    list_per_page = 10

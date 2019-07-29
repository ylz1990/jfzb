from django.contrib import admin
from .models import News,NewType
# Register your models here.

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("id","title","author","read_num","created_time")

@admin.register(NewType)
class NewType(admin.ModelAdmin):
    list_display = ("id","type_name")

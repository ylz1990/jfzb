from django.contrib import admin
from .models import CaseType,Case
# Register your models here.

@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ("id","title","author","read_num","created_time")

@admin.register(CaseType)
class CaseTypeAdmin(admin.ModelAdmin):
    list_display = ("id","case_type")

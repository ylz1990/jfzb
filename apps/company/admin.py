from django.contrib import admin
from .models import CompanyType,Company
# Register your models here.

@admin.register(CompanyType)
class CompanyTypeAdmin(admin.ModelAdmin):
    list_display = ["id","company_type"]

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["id","author","company_type","created_time"]



from django.contrib import admin
from .models import MemberType,Member
# Register your models here.

@admin.register(MemberType)
class MemberType(admin.ModelAdmin):
    list_display = ("id","member_type")



@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("id","title","author","read_num","created_time")
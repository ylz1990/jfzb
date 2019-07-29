from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class CompanyType(models.Model):
    company_type = models.CharField(max_length=20,verbose_name="公司",help_text="公司")

    def __str__(self):
        return self.company_type

class Company(models.Model):
    content = RichTextUploadingField(verbose_name='文章')
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name="作者")
    image_url = models.ImageField(upload_to="company", default='', blank=True)
    company_type = models.ForeignKey(CompanyType,on_delete=models.DO_NOTHING,verbose_name="君枫珠宝")

    class Meta:
        ordering = ["created_time"]
        db_table = "tb_company"
        verbose_name = "君枫珠宝"
        verbose_name_plural = verbose_name
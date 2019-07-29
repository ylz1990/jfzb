from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class CaseType(models.Model):
    case_type = models.CharField(max_length=20,verbose_name="大咖论道",help_text="大咖论道 ")

    def __str__(self):
        return self.case_type

class Case(models.Model):
    title = models.CharField(max_length=50,verbose_name="标题",help_text="标题")
    content = RichTextUploadingField(verbose_name="内容",help_text='内容')
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间",help_text="创建时间")
    read_num = models.IntegerField(default=0, verbose_name="阅读次数", help_text="阅读次数")
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name="作者", help_text="作者")
    case_type = models.ForeignKey(CaseType,on_delete=models.DO_NOTHING,verbose_name="大咖论道", help_text="大咖论道")
    image_url = models.ImageField(upload_to="case", default="", blank=True) # upload_to指定图片上传的途径，如果不存在则自动创建

    def __str__(self):
        return "<Case: %s>" % self.title

    class Meta:
        ordering = ["id", '-created_time']
        db_table = "tb_cases"  # 指明数据库表名
        verbose_name = "大咖论道"  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称
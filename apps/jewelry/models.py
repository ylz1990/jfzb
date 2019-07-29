from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class JewelryType(models.Model):
    jewelry_type = models.CharField(max_length=20,verbose_name="珠宝类型",help_text="珠宝类型")

    def __str__(self):
        return self.jewelry_type


class Jewelry(models.Model):
    title = models.CharField(max_length=50,verbose_name="标题",help_text="珠宝类型")
    content = RichTextUploadingField(verbose_name="文章",help_text="文章")
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="发布时间", help_text="发布时间")
    image_url = models.ImageField(upload_to='jewelry', default="", blank=True)  # upload_to指定图片上传的途径，如果不存在则自动创建
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="作者", help_text="作者")
    jewelry_type = models.ForeignKey(JewelryType, on_delete=models.DO_NOTHING, verbose_name="新闻类型", help_text="新闻类型")
    read_num = models.IntegerField(default=0, verbose_name="阅读次数", help_text="阅读次数")

    def __str__(self):
        return "<Jewelry: %s>" % self.title

    class Meta:
        ordering = ["id",'-created_time']
        db_table = "tb_jewelry"  # 指明数据库表名
        verbose_name = "珠宝资讯"  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称
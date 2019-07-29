from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

class NewType(models.Model):
    type_name = models.CharField(max_length=15,verbose_name="新闻类型", help_text="新闻类型")

    def __str__(self):
        return self.type_name

class News(models.Model):
    title = models.CharField(max_length=50,verbose_name="标题", help_text="标题")
    new_type = models.ForeignKey(NewType, on_delete=models.DO_NOTHING,verbose_name="新闻类型", help_text="新闻类型")
    content = RichTextUploadingField(verbose_name="文章", help_text="文章")
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING,verbose_name="作者", help_text="作者")
    read_num = models.IntegerField(default=0,verbose_name="阅读次数", help_text="阅读次数")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="发布时间", help_text="发布时间")

    def __str__(self):
        return "<New: %s>,<new_type: %s>" % (self.title,self.new_type)

    class Meta:
        ordering = ["id",'-created_time']
        db_table = "tb_news"  # 指明数据库表名
        verbose_name = "新闻"  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

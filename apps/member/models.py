from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class MemberType(models.Model):
    member_type = models.CharField(max_length=20,verbose_name="会员尊享",help_text="会员尊享")

    def __str__(self):
        return self.member_type

class Member(models.Model):
    title = models.CharField(max_length=50,verbose_name="标题",help_text="标题")
    content = RichTextUploadingField(verbose_name='文章',help_text='文章')
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="发布时间", help_text="发布时间")
    read_num = models.IntegerField(default=0,verbose_name="阅读量",help_text="阅读量")
    image_url = models.ImageField(upload_to="member",default='',blank=True)
    author = models.ForeignKey(User,verbose_name="作者",help_text="作者",on_delete=models.DO_NOTHING)
    member_type = models.ForeignKey(MemberType,on_delete=models.DO_NOTHING,verbose_name="会员尊享",help_text="会员尊享")

    def __str__(self):
        return "<Member: %s>" % self.title

    class Meta:
        ordering = ["id","created_time"]
        db_table = "tb_member"
        verbose_name = "会员尊享"  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

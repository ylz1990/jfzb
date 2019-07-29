# Generated by Django 2.0 on 2019-07-17 15:00

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Jewelry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='珠宝类型', max_length=50, verbose_name='标题')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(help_text='文章', verbose_name='文章')),
                ('created_time', models.DateTimeField(auto_now_add=True, help_text='发布时间', verbose_name='发布时间')),
                ('image_url', models.ImageField(blank=True, default='', upload_to='jewelry')),
                ('read_num', models.IntegerField(default=0, help_text='阅读次数', verbose_name='阅读次数')),
                ('author', models.ForeignKey(help_text='作者', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name': '珠宝资讯',
                'verbose_name_plural': '珠宝资讯',
                'db_table': 'tb_jewelry',
                'ordering': ['id', '-created_time'],
            },
        ),
        migrations.CreateModel(
            name='JewelryType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jewelry_type', models.CharField(help_text='珠宝类型', max_length=20, verbose_name='珠宝类型')),
            ],
        ),
        migrations.AddField(
            model_name='jewelry',
            name='jewelry_type',
            field=models.ForeignKey(help_text='新闻类型', on_delete=django.db.models.deletion.DO_NOTHING, to='jewelry.JewelryType', verbose_name='新闻类型'),
        ),
    ]

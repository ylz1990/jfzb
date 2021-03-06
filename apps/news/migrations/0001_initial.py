# Generated by Django 2.0 on 2019-07-14 17:40

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
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='标题', max_length=50, verbose_name='标题')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(help_text='文章', verbose_name='文章')),
                ('read_num', models.IntegerField(default=0, help_text='阅读次数', verbose_name='阅读次数')),
                ('created_time', models.DateTimeField(auto_now_add=True, help_text='发布时间', verbose_name='发布时间')),
                ('author', models.ForeignKey(help_text='作者', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name': '新闻',
                'verbose_name_plural': '新闻',
                'db_table': 'tb_news',
                'ordering': ['id', '-created_time'],
            },
        ),
        migrations.CreateModel(
            name='NewType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(help_text='新闻类型', max_length=15, verbose_name='新闻类型')),
            ],
        ),
        migrations.AddField(
            model_name='news',
            name='new_type',
            field=models.ForeignKey(help_text='新闻类型', on_delete=django.db.models.deletion.DO_NOTHING, to='news.NewType', verbose_name='新闻类型'),
        ),
    ]

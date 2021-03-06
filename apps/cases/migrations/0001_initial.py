# Generated by Django 2.0 on 2019-07-18 15:17

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
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='标题', max_length=50, verbose_name='标题')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(help_text='内容', verbose_name='内容')),
                ('created_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('read_num', models.IntegerField(default=0, help_text='阅读次数', verbose_name='阅读次数')),
                ('image_url', models.ImageField(blank=True, default='', upload_to='case')),
                ('author', models.ForeignKey(help_text='作者', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name': '大咖论道',
                'verbose_name_plural': '大咖论道',
                'db_table': 'tb_cases',
                'ordering': ['id', '-created_time'],
            },
        ),
        migrations.CreateModel(
            name='CaseType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_type', models.CharField(help_text='大咖论道 ', max_length=20, verbose_name='大咖论道')),
            ],
        ),
        migrations.AddField(
            model_name='case',
            name='case_type',
            field=models.ForeignKey(help_text='大咖论道', on_delete=django.db.models.deletion.DO_NOTHING, to='cases.CaseType', verbose_name='大咖论道'),
        ),
    ]

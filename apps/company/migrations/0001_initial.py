# Generated by Django 2.0 on 2019-07-25 18:03

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
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='文章')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('image_url', models.ImageField(blank=True, default='', upload_to='company')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name': '君枫珠宝',
                'verbose_name_plural': '君枫珠宝',
                'db_table': 'tb_company',
                'ordering': ['created_time'],
            },
        ),
        migrations.CreateModel(
            name='CompanyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_type', models.CharField(help_text='公司', max_length=20, verbose_name='公司')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='company_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='company.CompanyType', verbose_name='君枫珠宝'),
        ),
    ]

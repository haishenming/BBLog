# Generated by Django 2.0.2 on 2018-03-09 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='created',
            field=models.DateTimeField(auto_now=True, verbose_name='创建时间'),
        ),
    ]

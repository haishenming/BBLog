# Generated by Django 2.0.2 on 2018-03-09 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(blank=True, max_length=50, verbose_name='昵称'),
        ),
    ]

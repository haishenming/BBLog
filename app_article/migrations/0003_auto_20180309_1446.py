# Generated by Django 2.0.2 on 2018-03-09 06:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_article', '0002_article_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('created_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('created_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
        ),
        migrations.RenameField(
            model_name='article',
            old_name='created',
            new_name='created_time',
        ),
        migrations.AddField(
            model_name='article',
            name='update_time',
            field=models.DateTimeField(null=True, verbose_name='修改时间'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_article.Category', verbose_name='类别'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(null=True, to='app_article.Tag', verbose_name='标签'),
        ),
    ]
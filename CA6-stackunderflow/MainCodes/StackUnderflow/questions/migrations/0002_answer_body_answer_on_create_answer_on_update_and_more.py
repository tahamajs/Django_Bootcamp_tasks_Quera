# Generated by Django 4.1.4 on 2023-09-21 15:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='body',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='on_create',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='on_update',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='questions.question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='vote',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='body',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='on_create',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='on_update',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(blank=True, to='questions.tag'),
        ),
        migrations.AddField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='vote',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

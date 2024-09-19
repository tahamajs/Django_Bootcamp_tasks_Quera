# Generated by Django 4.1.4 on 2023-09-24 09:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0002_answer_body_answer_on_create_answer_on_update_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='vote',
        ),
        migrations.AddField(
            model_name='question',
            name='downvoters',
            field=models.ManyToManyField(blank=True, related_name='downvoted_questions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='upvoters',
            field=models.ManyToManyField(blank=True, related_name='upvoted_questions', to=settings.AUTH_USER_MODEL),
        ),
    ]

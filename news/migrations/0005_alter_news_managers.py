# Generated by Django 4.2.7 on 2024-02-22 11:28

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_news_options_alter_news_publish_time'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='news',
            managers=[
                ('published', django.db.models.manager.Manager()),
            ],
        ),
    ]

# Generated by Django 3.2 on 2021-04-15 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_article_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image_show',
            field=models.URLField(blank=True, null=True),
        ),
    ]

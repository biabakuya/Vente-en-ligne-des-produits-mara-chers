# Generated by Django 4.2.6 on 2023-12-13 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ndk_app', '0003_article_categorie'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

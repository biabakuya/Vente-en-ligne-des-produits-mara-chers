# Generated by Django 4.2.6 on 2024-01-28 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ndk_app', '0013_article_lien_paiement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='categorie',
        ),
    ]
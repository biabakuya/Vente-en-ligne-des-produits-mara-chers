# Generated by Django 4.2.6 on 2023-12-15 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ndk_app', '0005_alter_customuser_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail_commande',
            name='qte',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='panier',
            name='qte',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

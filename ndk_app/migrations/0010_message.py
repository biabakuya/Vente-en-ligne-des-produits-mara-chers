# Generated by Django 4.2.6 on 2024-01-20 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ndk_app', '0009_alter_customuser_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noms_complet', models.CharField(blank=True, max_length=255, null=True)),
                ('telephone', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('message', models.TextField(blank=True, null=True)),
            ],
        ),
    ]

# Generated by Django 3.2.25 on 2024-06-01 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_service_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='barber',
            name='social_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='barber',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]

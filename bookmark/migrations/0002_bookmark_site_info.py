# Generated by Django 3.0.2 on 2020-01-15 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='site_info',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]

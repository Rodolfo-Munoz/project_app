# Generated by Django 3.1.7 on 2021-06-16 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roseleaf_app', '0018_auto_20210406_2011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='Ingredients',
        ),
        migrations.AddField(
            model_name='recipe',
            name='Ingredients',
            field=models.CharField(default=None, max_length=300),
            preserve_default=False,
        ),
    ]

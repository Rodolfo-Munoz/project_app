# Generated by Django 3.1.7 on 2021-06-21 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roseleaf_app', '0019_auto_20210616_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='temprecords',
            name='temp_date',
            field=models.DateField(),
        ),
    ]

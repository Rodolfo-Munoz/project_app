# Generated by Django 3.1.7 on 2021-04-06 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roseleaf_app', '0014_delete_season'),
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]

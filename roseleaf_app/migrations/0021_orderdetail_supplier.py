# Generated by Django 3.1.7 on 2021-06-26 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roseleaf_app', '0020_auto_20210621_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='supplier',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='roseleaf_app.supplier'),
        ),
    ]

# Generated by Django 3.1.7 on 2021-03-20 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allergen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergen_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Fridge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fridge_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TempRecords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp_date', models.DateTimeField()),
                ('temperature', models.IntegerField()),
                ('fridge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roseleaf_app.fridge')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roseleaf_app.member')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('Ingredients', models.CharField(max_length=200)),
                ('method', models.CharField(max_length=300)),
                ('allergen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roseleaf_app.allergen')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roseleaf_app.member')),
            ],
        ),
    ]

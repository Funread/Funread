# Generated by Django 4.0.2 on 2023-10-11 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Grades', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grades',
            name='isactive',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.0.2 on 2022-11-16 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Grades', '0003_alter_grades_iduser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grades',
            name='booksid',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]

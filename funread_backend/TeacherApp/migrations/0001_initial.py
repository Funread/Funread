# Generated by Django 4.0.2 on 2023-09-22 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('TeacherId', models.AutoField(primary_key=True, serialize=False)),
                ('TeacherName', models.CharField(max_length=500)),
                ('TeacherPwd', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'teacher',
            },
        ),
    ]

# Generated by Django 4.0.2 on 2022-11-10 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Grades', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grades',
            old_name='BooksID',
            new_name='booksid',
        ),
        migrations.RenameField(
            model_name='grades',
            old_name='Grade',
            new_name='grade',
        ),
        migrations.RenameField(
            model_name='grades',
            old_name='GradesID',
            new_name='gradesid',
        ),
        migrations.RenameField(
            model_name='grades',
            old_name='Progress',
            new_name='progress',
        ),
    ]

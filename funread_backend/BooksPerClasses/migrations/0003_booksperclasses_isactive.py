# Generated by Django 4.0.2 on 2023-10-13 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BooksPerClasses', '0002_booksperclasses_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='booksperclasses',
            name='isactive',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

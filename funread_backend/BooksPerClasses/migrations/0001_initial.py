# Generated by Django 4.0.2 on 2022-11-17 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Classes', '0002_alter_classes_name'),
        ('Books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BooksPerClasses',
            fields=[
                ('booksPerClassesId', models.AutoField(primary_key=True, serialize=False)),
                ('bookId', models.ForeignKey(db_column='bookId', on_delete=django.db.models.deletion.CASCADE, related_name='bookIdBooksPerClasses', to='Books.book')),
                ('classesId', models.ForeignKey(db_column='classesId', on_delete=django.db.models.deletion.CASCADE, related_name='classesIdBooksPerClasses', to='Classes.classes')),
            ],
        ),
    ]

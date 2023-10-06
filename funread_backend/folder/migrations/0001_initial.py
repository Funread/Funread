# Generated by Django 4.0.2 on 2023-10-06 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('foldersid', models.AutoField(db_column='FoldersId', primary_key=True, serialize=False)),
                ('namefolders', models.CharField(db_column='NameFolders', max_length=200)),
                ('createdBy', models.ForeignKey(db_column='createdBy', on_delete=django.db.models.deletion.CASCADE, to='Users.user')),
            ],
            options={
                'db_table': 'folders',
            },
        ),
    ]

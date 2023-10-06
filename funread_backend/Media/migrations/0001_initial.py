# Generated by Django 4.0.2 on 2023-10-06 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('extension', models.CharField(max_length=10)),
                ('image', models.ImageField(blank='', default='', upload_to='media/')),
            ],
            options={
                'db_table': 'media',
            },
        ),
    ]

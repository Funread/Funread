# Generated by Django 4.0.2 on 2023-09-28 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(db_column='UserName', max_length=200, null=True, unique=True),
        ),
    ]

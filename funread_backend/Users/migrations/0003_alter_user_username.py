# Generated by Django 4.0.2 on 2023-09-29 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(db_column='UserName', max_length=200, unique=True),
        ),
    ]

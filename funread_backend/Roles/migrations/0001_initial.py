# Generated by Django 4.0.2 on 2023-10-06 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('rolesid', models.AutoField(db_column='RolesId', primary_key=True, serialize=False)),
                ('role', models.CharField(db_column='Role', max_length=200, unique=True)),
            ],
            options={
                'db_table': 'roles',
            },
        ),
    ]

# Generated by Django 4.0.2 on 2023-10-05 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('instituteid', models.AutoField(db_column='InstituteId', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=200, unique=True)),
            ],
            options={
                'db_table': 'institute',
            },
        ),
        migrations.CreateModel(
            name='InstituteMembers',
            fields=[
                ('institutemembersid', models.AutoField(db_column='InstituteMembersID', primary_key=True, serialize=False)),
                ('instituteid', models.ForeignKey(db_column='InstituteID', on_delete=django.db.models.deletion.CASCADE, to='Institute.institute')),
                ('userid', models.ForeignKey(db_column='UserId', on_delete=django.db.models.deletion.CASCADE, to='Users.user')),
            ],
            options={
                'db_table': 'institutemembers',
            },
        ),
    ]

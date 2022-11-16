# Generated by Django 4.0.2 on 2022-11-14 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentsGroups',
            fields=[
                ('groupId', models.AutoField(primary_key=True, serialize=False)),
                ('isTeacher', models.IntegerField(blank=True, db_column='isTeacher', null=True)),
                ('createdAt', models.DateTimeField(blank=True, db_column='createdAt', null=True)),
                ('createdBy', models.ForeignKey(db_column='createdBy', on_delete=django.db.models.deletion.CASCADE, related_name='createdByModel', to='Users.user')),
                ('userId', models.ForeignKey(db_column='idUser', on_delete=django.db.models.deletion.CASCADE, related_name='idUser', to='Users.user')),
            ],
        ),
    ]

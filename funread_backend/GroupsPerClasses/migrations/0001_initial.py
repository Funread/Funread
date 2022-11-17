# Generated by Django 4.0.2 on 2022-11-17 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('StudentsGroups', '0002_alter_studentsgroups_userid'),
        ('Classes', '0002_alter_classes_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupsPerClasses',
            fields=[
                ('groupsPerClassesId', models.AutoField(primary_key=True, serialize=False)),
                ('classesId', models.ForeignKey(db_column='classesId', on_delete=django.db.models.deletion.CASCADE, related_name='classesIdmodels', to='Classes.classes')),
                ('groupId', models.ForeignKey(db_column='groupId', on_delete=django.db.models.deletion.CASCADE, related_name='groupIdmodels', to='StudentsGroups.studentsgroups')),
            ],
        ),
    ]

# Generated by Django 4.0.2 on 2023-10-17 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '0001_initial'),
        ('GroupsCreate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentsGroups',
            fields=[
                ('studentsgroupsid', models.AutoField(db_column='StudentsGroupsId', primary_key=True, serialize=False)),
                ('isteacher', models.IntegerField(blank=True, db_column='isTeacher', null=True)),
                ('createdat', models.DateTimeField(blank=True, db_column='CreatedAt', null=True)),
                ('createdby', models.ForeignKey(db_column='CreatedBy', on_delete=django.db.models.deletion.CASCADE, related_name='created_student_groups', to='Users.user')),
                ('groupscreateid', models.ForeignKey(db_column='GroupsCreateId', on_delete=django.db.models.deletion.CASCADE, related_name='groupscreate', to='GroupsCreate.groupscreate')),
                ('userid', models.ForeignKey(db_column='UserId', on_delete=django.db.models.deletion.CASCADE, related_name='student_groups', to='Users.user')),
            ],
            options={
                'db_table': 'studentgroups',
                'unique_together': {('userid', 'groupscreateid')},
            },
        ),
    ]

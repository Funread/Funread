# Generated by Django 4.0.2 on 2023-09-29 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GroupsCreate', '0002_remove_groupscreate_image_groupscreate_idimage_and_more'),
        ('Users', '0003_alter_user_username'),
        ('StudentsGroups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentsgroups',
            name='groupscreateid',
            field=models.ForeignKey(db_column='GroupsCreateId', default=1, on_delete=django.db.models.deletion.CASCADE, related_name='groupscreate', to='GroupsCreate.groupscreate'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='studentsgroups',
            unique_together={('userid', 'groupscreateid')},
        ),
    ]

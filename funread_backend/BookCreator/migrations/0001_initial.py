# Generated by Django 4.0.2 on 2022-05-03 00:09

from django.db import migrations, models
from Users.models import User

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '__first__')
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bookid', models.AutoField(primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('category',models.IntegerField(blank=True,null=True)),
                ('portrait', models.CharField(max_length=200, blank=True)),
                ('createdBy',models.ForeignKey(to='User',related_name='user_that_create_it', on_delete=models.CASCADE)),
                ('createdAt',models.DateTimeField(blank=True, null=True)),
                ('updatedBy', models.ForeignKey(to='modeks.User',related_name='user_that_update_it', on_delete=models.CASCADE)),
                ('updatedAt', models.DateTimeField(blank=True, null=True)),
                ('state',models.IntegerField(blank=True)),
                ('sharedBook', models.BooleanField(default=False, blank=True, null=True)),
            ],
        )
    ]

# Generated by Django 4.0.2 on 2022-11-02 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('lastname', models.CharField(blank=True, max_length=200, null=True)),
                ('password', models.CharField(blank=True, max_length=256, null=True)),
                ('createdat', models.DateTimeField(blank=True, null=True)),
                ('actived', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]

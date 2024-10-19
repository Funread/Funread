# Generated by Django 4.0.2 on 2024-10-18 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=255)),
                ('points', models.IntegerField(db_column='Points')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='CreatedAt')),
                ('last_updated', models.DateTimeField(auto_now=True, db_column='LastUpdated')),
            ],
            options={
                'db_table': 'team',
            },
        ),
    ]

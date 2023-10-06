# Generated by Django 4.0.2 on 2023-10-06 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Widget',
            fields=[
                ('widgetid', models.AutoField(db_column='WidgetId', primary_key=True, serialize=False)),
                ('type', models.IntegerField(blank=True, db_column='Type', null=True)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=200, null=True)),
            ],
            options={
                'db_table': 'widget',
            },
        ),
        migrations.CreateModel(
            name='WidgetItem',
            fields=[
                ('widgetitemid', models.AutoField(db_column='WidgetItemId', primary_key=True, serialize=False)),
                ('value', models.IntegerField(blank=True, db_column='Value', null=True)),
                ('type', models.IntegerField(blank=True, db_column='Type', null=True)),
                ('pageid', models.ForeignKey(blank=True, db_column='PageId', null=True, on_delete=django.db.models.deletion.CASCADE, to='Pages.pages')),
                ('widgetid', models.ForeignKey(blank=True, db_column='WidgetId', null=True, on_delete=django.db.models.deletion.CASCADE, to='Widget.widget')),
            ],
            options={
                'db_table': 'widgetitem',
            },
        ),
    ]
